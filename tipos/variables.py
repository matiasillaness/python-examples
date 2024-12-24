""""Variables en Python"""

# Lista completa de tipos de variables en Python con ejemplos y comentarios

# 1. Tipos primitivos

# 1.1 Entero (int): Números enteros, positivos o negativos, sin decimales.
numero = 10  # Ejemplo de número entero
negativo = -5  # Ejemplo de número entero negativo

# 1.2 Decimal (float): Números con punto flotante (decimales).
pi = 3.14  # Ejemplo de número decimal

# 1.3 Número complejo (complex): Números con parte real e imaginaria.
complejo = 2 + 3j  # Parte real = 2, parte imaginaria = 3j

# 1.4 Cadena de texto (str): Secuencia de caracteres.
texto = "Hola, Mundo"  # Ejemplo de cadena de texto

# 1.5 Booleano (bool): Valores de verdad, True o False.
es_verdadero = True  # Ejemplo de booleano verdadero
es_falso = False  # Ejemplo de booleano falso

# 2. Tipos de datos compuestos

# 2.1 Lista (list): Secuencia ordenada y mutable.
mi_lista = [1, 2, 3, "hola"]  # Puede contener diferentes tipos de datos

# 2.2 Tupla (tuple): Secuencia ordenada e inmutable.
mi_tupla = (1, 2, 3)  # Los elementos no se pueden modificar

# 2.3 Conjunto (set): Colección no ordenada de elementos únicos.
mi_set = {1, 2, 3, 4}  # No permite elementos repetidos

# 2.4 Diccionario (dict): Pares clave-valor.
mi_diccionario = {"nombre": "Ana", "edad": 25}  # Claves únicas con valores asociados

# 3. Variables especiales

# 3.1 Ningún valor o nulo (NoneType): Representa la ausencia de un valor.
nada = None  # Similar a "null" en otros lenguajes

# 4. Asignación múltiple

# 4.1 Asignar múltiples valores a múltiples variables en una línea.
a, b, c = 1, 2, 3  # Asigna 1 a 'a', 2 a 'b', 3 a 'c'

# 4.2 Asignar el mismo valor a múltiples variables.
x = y = z = 0  # Todas las variables valen 0

# 5. Variables globales y locales

# 5.1 Variable global: Declarada fuera de funciones, accesible en todo el programa.
global_variable = "Soy global"

def mi_funcion():
    # 5.2 Variable local: Declarada dentro de una función, solo accesible ahí.
    local_variable = "Soy local"
    print(local_variable)  # Acceso válido dentro de la función

mi_funcion()
print(global_variable)  # Acceso válido fuera de la función

# Para modificar una variable global dentro de una función, se usa la palabra clave 'global'.
def modificar_global():
    global global_variable
    global_variable = "He cambiado globalmente"

modificar_global()
print(global_variable)  # Ahora la variable global tiene un nuevo valor

# 6. Constantes (simuladas)
# Python no tiene constantes reales, pero se usan nombres en mayúsculas por convención.
PI = 3.14159  # Por convención, las constantes se escriben en mayúsculas
GRAVEDAD = 9.81  # Ejemplo de constante

# 7. Buenas prácticas para nombres de variables
# - Usar nombres descriptivos.
# - Evitar palabras reservadas (como if, for, class).
# - Seguir el estilo snake_case.
contador_usuarios = 100  # Ejemplo de nombre descriptivo y en snake_case
