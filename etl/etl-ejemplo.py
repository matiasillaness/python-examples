# -----------------------------------------------------
# EJEMPLO 1: Proceso ETL Básico
# -----------------------------------------------------
# Este ejemplo extrae datos de un archivo CSV, los transforma
# y los guarda en un nuevo archivo CSV.

import pandas as pd

# Paso 1: Extracción
# Leer datos desde un archivo CSV
print("Extrayendo datos desde 'productos.csv'...")
data = pd.read_csv("productos.csv")  # Archivo CSV de ejemplo
print(data.head())  # Ver las primeras filas

# Paso 2: Transformación
# Agregar una nueva columna que calcule el precio con IVA (21%)
print("Transformando los datos...")
data["precio_con_iva"] = data["precio"] * 1.21

# Renombrar la columna "nombre" a "producto"
data.rename(columns={"nombre": "producto"}, inplace=True)
print(data.head())

# Paso 3: Carga
# Guardar los datos transformados en un nuevo archivo CSV
print("Cargando los datos en 'productos_transformados.csv'...")
data.to_csv("productos_transformados.csv", index=False)
print("Proceso ETL Básico completado.")

# -----------------------------------------------------
# EJEMPLO 2: Proceso ETL Complejo
# -----------------------------------------------------
# Este ejemplo extrae datos de una API, los transforma en un DataFrame
# y los carga en una base de datos PostgreSQL.

import requests
from sqlalchemy import create_engine

# Paso 1: Extracción
# Extraer datos de una API
print("Extrayendo datos desde la API...")
url = "https://jsonplaceholder.typicode.com/posts"  # API de ejemplo
response = requests.get(url)
if response.status_code == 200:
    raw_data = response.json()
    print("Datos extraídos con éxito.")
else:
    raise Exception(f"Error en la API: {response.status_code}")

# Paso 2: Transformación
# Convertir los datos en un DataFrame para procesarlos
print("Transformando los datos...")
data = pd.DataFrame(raw_data)

# Seleccionar solo las columnas relevantes
data = data[["userId", "id", "title", "body"]]
data.columns = ["usuario_id", "id_publicacion", "titulo", "contenido"]

# Agregar una columna que calcule la longitud del contenido
data["longitud_contenido"] = data["contenido"].apply(len)
print(data.head())

# Paso 3: Carga
# Cargar los datos transformados en una base de datos PostgreSQL
print("Cargando los datos en la base de datos...")
conexion_string = "postgresql://usuario:password@localhost:5432/mi_base_datos"
engine = create_engine(conexion_string)

data.to_sql("publicaciones", engine, if_exists="replace", index=False)
print("Datos cargados en la tabla 'publicaciones'.")

print("Proceso ETL Complejo completado.")
