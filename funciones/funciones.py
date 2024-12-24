# -----------------------------------------------------
# 1. FUNCIONES BÁSICAS
# -----------------------------------------------------

# Definir una función con 'def'
def saludar():
    """
    Esta función no recibe parámetros y solo imprime un saludo.
    """
    print("Hola, bienvenido a Python!")

# Llamar a la función
saludar()

# -----------------------------------------------------
# 2. FUNCIONES CON PARÁMETROS
# -----------------------------------------------------

# Función con un parámetro
def saludar_persona(nombre):
    """
    Recibe un nombre como argumento y lo utiliza en un saludo.
    """
    print(f"Hola, {nombre}! ¿Cómo estás?")

# Llamar a la función con un argumento
saludar_persona("Matías")

# Función con múltiples parámetros
def sumar(a, b):
    """
    Suma dos números y devuelve el resultado.
    """
    return a + b

# Llamar a la función y almacenar el resultado
resultado = sumar(5, 7)
print(f"El resultado de la suma es: {resultado}")

# -----------------------------------------------------
# 3. PARÁMETROS POR DEFECTO
# -----------------------------------------------------

def saludar_con_tono(nombre, tono="formal"):
    """
    Realiza un saludo con un tono que puede ser 'formal' o 'informal'.
    Si no se especifica, el tono es 'formal'.
    """
    if tono == "formal":
        print(f"Buenas tardes, {nombre}.")
    else:
        print(f"¡Qué tal, {nombre}!")

# Usar la función con y sin el parámetro opcional
saludar_con_tono("Carlos")  # Tono por defecto
saludar_con_tono("Carlos", tono="informal")

# -----------------------------------------------------
# 4. FUNCIONES CON NÚMERO VARIABLE DE ARGUMENTOS
# -----------------------------------------------------

# *args: Recibe cualquier cantidad de argumentos posicionales
def sumar_todos(*numeros):
    """
    Suma todos los números que recibe como argumentos.
    """
    return sum(numeros)

# Llamar a la función con diferentes cantidades de argumentos
print(sumar_todos(1, 2, 3))  # Resultado: 6
print(sumar_todos(4, 5, 6, 7))  # Resultado: 22

# **kwargs: Recibe argumentos con clave-valor
def describir_persona(**datos):
    """
    Muestra información de una persona usando argumentos clave-valor.
    """
    for clave, valor in datos.items():
        print(f"{clave.capitalize()}: {valor}")

# Llamar a la función con argumentos clave-valor
describir_persona(nombre="Laura", edad=30, ciudad="Córdoba")

# -----------------------------------------------------
# 5. FUNCIONES ANIDADAS
# -----------------------------------------------------

def operacion_compleja(x):
    """
    Realiza una operación compleja utilizando una función interna.
    """
    def cuadrado(n):
        return n ** 2  # Función anidada para calcular el cuadrado

    return cuadrado(x) + 10

# Llamar a la función
print(operacion_compleja(3))  # Resultado: 19 (3**2 + 10)

# -----------------------------------------------------
# 6. FUNCIONES LAMBDA (ANÓNIMAS)
# -----------------------------------------------------

# Función lambda básica
doble = lambda x: x * 2
print(doble(4))  # Resultado: 8

# Lambda con múltiples parámetros
multiplicar = lambda a, b: a * b
print(multiplicar(3, 5))  # Resultado: 15

# Uso de lambda con funciones como map, filter o sorted
numeros = [1, 2, 3, 4, 5]

# Multiplicar cada número por 2 usando map
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)  # Resultado: [2, 4, 6, 8, 10]

# Filtrar números impares usando filter
impares = list(filter(lambda x: x % 2 != 0, numeros))
print(impares)  # Resultado: [1, 3, 5]

# -----------------------------------------------------
# 7. DOCUMENTAR FUNCIONES
# -----------------------------------------------------

def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.

    Parámetros:
    - base (float): La base del rectángulo.
    - altura (float): La altura del rectángulo.

    Retorna:
    - float: El área calculada.
    """
    return base * altura

# Llamar a la función
area = calcular_area_rectangulo(5, 10)
print(f"El área del rectángulo es: {area}")

# -----------------------------------------------------
# 8. RECURSIVIDAD
# -----------------------------------------------------

def factorial(n):
    """
    Calcula el factorial de un número de manera recursiva.
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Llamar a la función
print(factorial(5))  # Resultado: 120 (5 * 4 * 3 * 2 * 1)
