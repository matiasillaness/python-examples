# 1. Importaciones estándar de Python
from datetime import datetime
from typing import Any, Dict, List
import os
# 2. Importaciones de terceros
import pandas as pd
import requests
from sqlalchemy import create_engine

class ETLPipeline:
    """Class representing a basic ETL pipeline."""
    def __init__(self, api_url: str, db_connection_string: str):
        """
        Inicializa el pipeline ETL para API pública.
        Args:
            api_url: URL de la API pública
            db_connection_string: String de conexión a la base de datos
        Raises:
            Exception: Si no se puede establecer la conexión con PostgreSQL
        """
        self.api_url = api_url
        try:
            self.engine = create_engine(db_connection_string)
            # Probar la conexión
            with self.engine.connect() as conn:
                pass
            print("Conexión a la base de datos establecida correctamente")
        except Exception as e:
            print(f"Error al conectar con PostgreSQL: {str(e)}")
            raise Exception("No se pudo establecer la conexión con PostgreSQL. Verifica las credenciales y que el servidor esté activo.")

    def extract(self) -> List[Dict[str, Any]]:
        """
        Extrae datos de usuarios de la API pública.
        Returns:
            List[Dict[str, Any]]: Lista de diccionarios con datos de usuarios
        Raises:
            Exception: Si hay un error en la llamada a la API
        """
        print("Iniciando extracción de datos...")
        response = requests.get(self.api_url)
        
        if response.status_code == 200:
            users_data = response.json()
            all_data = []
            
            for user in users_data:
                simplified_data = {
                    'id': user['id'],
                    'name': user['name'],
                    'username': user['username'],
                    'email': user['email'],
                    'phone': user['phone'],
                    'website': user['website'],
                    'company_name': user['company']['name'],
                    'address_city': user['address']['city'],
                    'address_street': user['address']['street'],
                    'address_suite': user['address']['suite'],
                    'address_zipcode': user['address']['zipcode']
                }
                all_data.append(simplified_data)
                print(f"Extraído usuario: {user['name']}")
                
            print(f"Extracción completada. Usuarios obtenidos: {len(all_data)}")
            return all_data
        else:
            raise Exception(f"Error en la API: {response.status_code}")

    def transform(self, data: List[Dict[str, Any]]) -> pd.DataFrame:
        """
        Transforma los datos extraídos.
        Args:
            data: Lista de diccionarios con datos de usuarios
        Returns:
            pd.DataFrame: DataFrame con los datos transformados
        """
        print("Iniciando transformación de datos...")
        df = pd.DataFrame(data)
        
        # Limpieza básica
        df['name'] = df['name'].str.strip()
        df['email'] = df['email'].str.lower()
        df['website'] = df['website'].str.lower()
        
        # Crear columna de dirección completa
        df['full_address'] = df['address_street'] + ', ' + \
                           df['address_suite'] + ', ' + \
                           df['address_city'] + ' ' + \
                           df['address_zipcode']
        
        # Agregar timestamp del ETL
        df['etl_timestamp'] = datetime.now()
        
        print(f"Transformación completada. Registros procesados: {len(df)}")
        return df

    def load(self, df: pd.DataFrame, table_name: str) -> None:
        """
        Carga los datos en la base de datos.
        Args:
            df: DataFrame con los datos a cargar
            table_name: Nombre de la tabla donde se cargarán los datos
        Raises:
            Exception: Si hay un error durante la carga de datos
        """
        print(f"Iniciando carga de datos en tabla {table_name}...")
        try:
            df.to_sql(
                name=table_name,
                con=self.engine,
                if_exists='replace',
                index=False,
                chunksize=1000
            )
            print(f"Datos cargados exitosamente. Registros insertados: {len(df)}")
        except Exception as e:
            print(f"Error en la carga: {str(e)}")
            raise

    def run_pipeline(self, table_name: str) -> None:
        """
        Ejecuta el pipeline ETL completo.
        Args:
            table_name: Nombre de la tabla donde se cargarán los datos
        Raises:
            Exception: Si hay un error en cualquier paso del pipeline
        """
        try:
            print("Iniciando pipeline ETL...")
            raw_data = self.extract()
            transformed_data = self.transform(raw_data)
            self.load(transformed_data, table_name)
            print("Pipeline ETL completado exitosamente!")
        except Exception as e:
            print(f"Error en el pipeline ETL: {str(e)}")
            raise

if __name__ == "__main__":
    # Configuración para la API de usuarios de JSONPlaceholder
    API_URL = "https://jsonplaceholder.typicode.com/users"
    DB_CONNECTION = "postgresql://postgres:example@localhost:5432/etl-user"
    TABLE_NAME = "users_data"
    
    # Crear y ejecutar pipeline
    pipeline = ETLPipeline(API_URL, DB_CONNECTION)
    pipeline.run_pipeline(TABLE_NAME)