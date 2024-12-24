# -----------------------------------------------------
# 1. ABRIR ARCHIVOS: MODOS
# -----------------------------------------------------

# Modos principales al abrir archivos:
# - "r": Leer (read) - El archivo debe existir.
# - "w": Escribir (write) - Crea o sobrescribe el archivo.
# - "a": Agregar (append) - Añade contenido al final del archivo.
# - "r+": Leer y escribir - No crea un archivo nuevo si no existe.
# - "b": Modo binario (puede combinarse, ej.: "rb", "wb").

# -----------------------------------------------------
# 2. ESCRIBIR ARCHIVOS
# -----------------------------------------------------

# Modo "w": Escribir un archivo nuevo (sobreescribe si existe).
with open("ejemplo.txt", "w") as archivo:
    archivo.write("Primera línea\n")  # Escribir una línea
    archivo.write("Segunda línea\n")  # Escribir otra línea

# Modo "a": Agregar contenido a un archivo existente.
with open("ejemplo.txt", "a") as archivo:
    archivo.write("Línea agregada con 'append'\n")

# -----------------------------------------------------
# 3. LEER ARCHIVOS
# -----------------------------------------------------

# Leer todo el contenido del archivo (modo "r").
with open("ejemplo.txt", "r") as archivo:
    contenido = archivo.read()  # Lee todo el archivo como una cadena
    print("Contenido completo:")
    print(contenido)

# Leer línea por línea usando un bucle.
with open("ejemplo.txt", "r") as archivo:
    print("Leyendo línea por línea:")
    for linea in archivo:
        print(linea.strip())  # Imprime cada línea sin saltos de línea extra

# Leer un número específico de caracteres.
with open("ejemplo.txt", "r") as archivo:
    print("Primeros 10 caracteres:")
    print(archivo.read(10))  # Lee los primeros 10 caracteres

# Leer todas las líneas como una lista.
with open("ejemplo.txt", "r") as archivo:
    lineas = archivo.readlines()  # Cada línea es un elemento de la lista
    print("Líneas como lista:")
    print(lineas)

# -----------------------------------------------------
# 4. MODO r+ (LEER Y ESCRIBIR)
# -----------------------------------------------------

# Leer y escribir en el mismo archivo (modo "r+").
with open("ejemplo.txt", "r+") as archivo:
    contenido = archivo.read()  # Leer el contenido existente
    archivo.write("\nNueva línea escrita con r+")  # Agregar nueva línea

# -----------------------------------------------------
# 5. MANEJO DE ERRORES AL TRABAJAR CON ARCHIVOS
# -----------------------------------------------------

# Usar try-except para manejar errores al trabajar con archivos.
try:
    with open("archivo_inexistente.txt", "r") as archivo:
        print(archivo.read())
except FileNotFoundError:
    print("Error: El archivo no existe.")
except IOError:
    print("Error: Problema al leer/escribir en el archivo.")

# -----------------------------------------------------
# 6. ARCHIVOS BINARIOS
# -----------------------------------------------------

# Escribir en modo binario.
with open("archivo_binario.dat", "wb") as archivo:
    archivo.write(b"Esto es binario")  # Prefijo 'b' indica datos binarios

# Leer en modo binario.
with open("archivo_binario.dat", "rb") as archivo:
    datos = archivo.read()
    print("Datos binarios:")
    print(datos)

# -----------------------------------------------------
# 7. GESTIÓN DE ARCHIVOS GRANDES
# -----------------------------------------------------

# Leer un archivo grande línea por línea (sin cargarlo todo en memoria).
with open("ejemplo.txt", "r") as archivo:
    print("Lectura eficiente de archivo grande:")
    for linea in archivo:
        print(linea.strip())

# -----------------------------------------------------
# 8. EJEMPLO COMPLETO: PROCESAR UN ARCHIVO DE TEXTO
# -----------------------------------------------------

# Crear un archivo y procesarlo.
with open("datos.txt", "w") as archivo:
    archivo.write("Python es divertido\n")
    archivo.write("Aprender a manejar archivos es útil\n")
    archivo.write("¡Practica mucho!\n")

# Contar palabras en el archivo.
with open("datos.txt", "r") as archivo:
    print("Procesando archivo para contar palabras:")
    for linea in archivo:
        palabras = linea.split()
        print(f"Línea: {linea.strip()} - Palabras: {len(palabras)}")

# -----------------------------------------------------
# 9. ELIMINAR O RENOMBRAR ARCHIVOS
# -----------------------------------------------------

import os

# Renombrar un archivo.
os.rename("datos.txt", "nuevo_datos.txt")

# Eliminar un archivo.
os.remove("nuevo_datos.txt")
print("Archivo eliminado.")
