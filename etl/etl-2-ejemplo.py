import requests  # Para realizar solicitudes HTTP (API)
import pandas as pd  # Para manipulación de datos en DataFrame
import psycopg2  # Para interactuar con la base de datos PostgreSQL
from datetime import datetime, timedelta  # Para manipular fechas y horas
import logging  # Para la gestión de logs
from typing import List, Dict, Any  # Para las anotaciones de tipos
from sqlalchemy import create_engine  # Para conectarse a PostgreSQL usando SQLAlchemy
from concurrent.futures import ThreadPoolExecutor  # Para la ejecución de tareas paralelas
import json  # Para manejar datos JSON
from retry import retry  # Para reintentar solicitudes fallidas
import os  # Para manejar variables de entorno
from dotenv import load_dotenv  # Para cargar las variables de entorno desde un archivo .env

# Configuración de logging: Permite registrar mensajes en archivo y consola
logging.basicConfig(
    level=logging.INFO,  # El nivel de detalle de los logs
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Formato del log
    handlers=[logging.FileHandler('etl.log'), logging.StreamHandler()]  # Salida en archivo y consola
)
logger = logging.getLogger(__name__)  # Se crea un logger para registrar los eventos

class WeatherDataETL:
    def __init__(self):
        load_dotenv()  # Carga las variables de entorno desde el archivo .env
        # Parámetros de la API y la base de datos, tomados desde las variables de entorno
        self.api_key = os.getenv('WEATHER_API_KEY')  
        self.db_params = {
            'host': os.getenv('DB_HOST', 'localhost'),
            'database': os.getenv('DB_NAME', 'weather_db'),
            'user': os.getenv('DB_USER', 'postgres'),
            'password': os.getenv('DB_PASSWORD'),
            'port': os.getenv('DB_PORT', '5432')
        }
        # Lista de ciudades con sus coordenadas (latitud y longitud)
        self.cities = [
            {'name': 'Madrid', 'lat': 40.4168, 'lon': -3.7038},
            {'name': 'Barcelona', 'lat': 41.3851, 'lon': 2.1734},
            {'name': 'Valencia', 'lat': 39.4699, 'lon': -0.3763},
            {'name': 'Sevilla', 'lat': 37.3891, 'lon': -5.9845}
        ]

    # Función de reintento para manejar fallos de la API (hasta 3 intentos)
    @retry(tries=3, delay=2, backoff=2)
    def extract_weather_data(self, city: Dict[str, Any]) -> Dict[str, Any]:
        """
        Extrae datos meteorológicos de la API OpenWeatherMap para una ciudad
        """
        url = f"https://api.openweathermap.org/data/2.5/weather"  # URL de la API
        params = {
            'lat': city['lat'],  # Latitud de la ciudad
            'lon': city['lon'],  # Longitud de la ciudad
            'appid': self.api_key,  # API Key para autenticar la solicitud
            'units': 'metric'  # Unidades métricas para la temperatura (Celsius)
        }
        
        try:
            response = requests.get(url, params=params, timeout=10)  # Realiza la solicitud GET
            response.raise_for_status()  # Verifica si hubo algún error en la respuesta
            data = response.json()  # Convierte la respuesta en formato JSON
            
            # Estructura los datos relevantes
            weather_data = {
                'city_name': city['name'],
                'temperature': data['main']['temp'],
                'feels_like': data['main']['feels_like'],
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'wind_speed': data['wind']['speed'],
                'description': data['weather'][0]['description'],
                'timestamp': datetime.utcfromtimestamp(data['dt']),
                'sunrise': datetime.utcfromtimestamp(data['sys']['sunrise']),
                'sunset': datetime.utcfromtimestamp(data['sys']['sunset'])
            }
            return weather_data  # Devuelve los datos de la ciudad
            
        except requests.exceptions.RequestException as e:  # Si hay error en la solicitud
            logger.error(f"Error extracting data for {city['name']}: {str(e)}")  # Registra el error
            raise  # Vuelve a lanzar la excepción

    def transform_weather_data(self, data: List[Dict[str, Any]]) -> pd.DataFrame:
        """
        Transforma los datos meteorológicos en un DataFrame de pandas
        """
        try:
            df = pd.DataFrame(data)  # Convierte la lista de diccionarios en DataFrame
            
            # Cálculos adicionales
            df['day_length'] = (df['sunset'] - df['sunrise']).dt.total_seconds() / 3600  # Duración del día en horas
            df['is_night'] = datetime.utcnow() > df['sunset']  # Verifica si es de noche
            df['temp_category'] = pd.cut(  # Categoriza la temperatura
                df['temperature'],
                bins=[-float('inf'), 10, 20, 30, float('inf')],
                labels=['Cold', 'Mild', 'Warm', 'Hot']
            )
            df['description'] = df['description'].str.title()  # Capitaliza la descripción del clima
            return df  # Devuelve el DataFrame transformado
            
        except Exception as e:  # En caso de error en la transformación
            logger.error(f"Error transforming weather data: {str(e)}")
            raise  # Vuelve a lanzar la excepción

    def load_to_postgres(self, df: pd.DataFrame) -> None:
        """
        Carga los datos transformados en la base de datos PostgreSQL
        """
        try:
            # Crea una conexión a la base de datos usando SQLAlchemy
            engine = create_engine(
                f"postgresql://{self.db_params['user']}:{self.db_params['password']}@"
                f"{self.db_params['host']}:{self.db_params['port']}/{self.db_params['database']}"
            )
            
            # Crea la tabla si no existe
            create_table_query = """
            CREATE TABLE IF NOT EXISTS weather_data (
                id SERIAL PRIMARY KEY,
                city_name VARCHAR(100),
                temperature FLOAT,
                feels_like FLOAT,
                humidity INTEGER,
                pressure INTEGER,
                wind_speed FLOAT,
                description VARCHAR(200),
                timestamp TIMESTAMP,
                sunrise TIMESTAMP,
                sunset TIMESTAMP,
                day_length FLOAT,
                is_night BOOLEAN,
                temp_category VARCHAR(50),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
            with engine.connect() as connection:
                connection.execute(create_table_query)  # Ejecuta la creación de la tabla
            
            # Inserta los datos en la base de datos
            df.to_sql('weather_data', engine, if_exists='append', index=False)
            logger.info(f"Successfully loaded {len(df)} records to PostgreSQL")  # Registra éxito
            
        except Exception as e:  # En caso de error al cargar los datos
            logger.error(f"Error loading data to PostgreSQL: {str(e)}")
            raise  # Vuelve a lanzar la excepción

    def run_etl(self):
        """
        Ejecuta el proceso ETL completo: extracción, transformación y carga
        """
        try:
            logger.info("Starting ETL process...")  # Registra inicio del proceso ETL
            
            # Realiza la extracción de datos de forma paralela para cada ciudad
            with ThreadPoolExecutor(max_workers=4) as executor:
                weather_data = list(executor.map(self.extract_weather_data, self.cities))
            
            transformed_data = self.transform_weather_data(weather_data)  # Transforma los datos
            self.load_to_postgres(transformed_data)  # Carga los datos transformados en la base de datos
            
            logger.info("ETL process completed successfully!")  # Registra éxito del proceso ETL
            
        except Exception as e:  # En caso de error en el proceso ETL
            logger.error(f"ETL process failed: {str(e)}")
            raise  # Vuelve a lanzar la excepción

# Ejecuta el script si se ejecuta directamente
if __name__ == "__main__":
    etl = WeatherDataETL()  # Crea una instancia de la clase WeatherDataETL
    etl.run_etl()  # Ejecuta el proceso ETL
