# -----------------------------------------------------
# 1. ¿QUÉ SON MÓDULOS?
# -----------------------------------------------------
# Un módulo en Python es un archivo que contiene código Python
# (funciones, clases, variables) que puedes importar y reutilizar.

# Crear un módulo llamado "mis_utilidades.py"
# Archivo: mis_utilidades.py
def saludar(nombre):
    """
    Función para saludar a una persona.
    """
    return f"Hola, {nombre}!"

def sumar(a, b):
    """
    Función para sumar dos números.
    """
    return a + b

PI = 3.14159  # Constante matemática

# -----------------------------------------------------
# 2. IMPORTAR MÓDULOS
# -----------------------------------------------------

# Puedes importar el módulo completo:
import mis_utilidades

# Usar funciones y variables del módulo.
print(mis_utilidades.saludar("Matías"))
print(mis_utilidades.sumar(3, 5))
print(f"El valor de PI es: {mis_utilidades.PI}")

# También puedes importar partes específicas:
from mis_utilidades import saludar, PI

print(saludar("Córdoba"))
print(f"Usando PI: {PI}")

# O importar todo el contenido con "*":
from mis_utilidades import *

print(sumar(10, 20))  # No necesitas prefijo del módulo

# -----------------------------------------------------
# 3. ¿QUÉ SON PAQUETES?
# -----------------------------------------------------
# Un paquete es una colección de módulos organizados en directorios.
# Debe contener un archivo especial llamado "__init__.py" (puede estar vacío o con lógica).

# Estructura de ejemplo:
# mi_paquete/
# ├── __init__.py
# ├── calculos.py
# └── textos.py

# Archivo: mi_paquete/calculos.py
def multiplicar(a, b):
    return a * b

# Archivo: mi_paquete/textos.py
def contar_palabras(frase):
    return len(frase.split())

# Archivo: mi_paquete/__init__.py
from .calculos import multiplicar
from .textos import contar_palabras

# -----------------------------------------------------
# 4. USAR PAQUETES
# -----------------------------------------------------

# Importar un paquete y usar sus módulos.
from mi_paquete import multiplicar, contar_palabras

print(multiplicar(4, 5))  # Resultado: 20
print(contar_palabras("Hola desde un paquete"))  # Resultado: 4

# También puedes importar módulos específicos del paquete.
from mi_paquete.calculos import multiplicar

print(multiplicar(6, 7))  # Resultado: 42

# -----------------------------------------------------
# 5. MÓDULOS Y PAQUETES ESTÁNDAR DE PYTHON
# -----------------------------------------------------

# Python incluye muchos módulos estándar que puedes usar sin instalar nada.
# Ejemplos comunes:

# Módulo math: Operaciones matemáticas avanzadas.
import math

print(f"Raíz cuadrada de 16: {math.sqrt(16)}")
print(f"Seno de 90 grados: {math.sin(math.radians(90))}")

# Módulo random: Generación de números aleatorios.
import random

print(f"Número aleatorio entre 1 y 10: {random.randint(1, 10)}")

# Módulo datetime: Manejo de fechas y horas.
import datetime

ahora = datetime.datetime.now()
print(f"Fecha y hora actuales: {ahora}")

# -----------------------------------------------------
# 6. INSTALAR Y USAR PAQUETES DE TERCEROS
# -----------------------------------------------------
# Usa el gestor de paquetes pip para instalar módulos y paquetes externos.
# Ejemplo: Instalar la biblioteca "requests" para hacer solicitudes HTTP.

# En la terminal:
# pip install requests

# Uso de requests:
import requests

respuesta = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(respuesta.json())

# -----------------------------------------------------
# 7. CREAR TU PROPIO PAQUETE INSTALABLE
# -----------------------------------------------------
# Para compartir tu paquete con otros, sigue estos pasos:

# 1. Crea una estructura de directorios similar a:
# mi_paquete/
# ├── mi_paquete/
# │   ├── __init__.py
# │   ├── calculos.py
# │   └── textos.py
# ├── setup.py
# └── README.md

# 2. Escribe el archivo setup.py:
"""
from setuptools import setup, find_packages

setup(
    name="mi_paquete",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],  # Lista de dependencias
)
"""

# 3. Instala localmente el paquete:
# En la terminal, ejecuta:
# pip install -e .

# -----------------------------------------------------
# 8. IMPORTACIÓN RELATIVA (DENTRO DE UN PAQUETE)
# -----------------------------------------------------
# Puedes usar importaciones relativas para acceder a módulos dentro del mismo paquete.

# En mi_paquete/textos.py
from .calculos import multiplicar

def texto_y_calculo(frase, a, b):
    """
    Combina texto y una operación matemática.
    """
    return f"{frase} - Resultado de multiplicar: {multiplicar(a, b)}"

# -----------------------------------------------------
# ¡PRUEBA ESTOS CONCEPTOS EN TU PROYECTO!
# -----------------------------------------------------
