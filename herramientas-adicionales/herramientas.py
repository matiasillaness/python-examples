# -----------------------------------------------------
# 1. LIST COMPREHENSIONS
# -----------------------------------------------------
# Es una forma concisa y eficiente de crear listas en Python.
# Sintaxis: [expresión for elemento in iterable if condición]

# Ejemplo básico: Crear una lista con los cuadrados de los números del 0 al 4.
cuadrados = [x**2 for x in range(5)]
print(cuadrados)  # Resultado: [0, 1, 4, 9, 16]

# Con condición (if): Incluir solo números pares y elevarlos al cuadrado.
pares_cuadrados = [x**2 for x in range(10) if x % 2 == 0]
print(pares_cuadrados)  # Resultado: [0, 4, 16, 36, 64]

# Con condición (if-else): Asignar un valor según la condición.
pares_impares = [x if x % 2 == 0 else -x for x in range(10)]
print(pares_impares)  # Resultado: [0, -1, 2, -3, 4, -5, 6, -7, 8, -9]

# List comprehension anidada: Matriz (tabla de multiplicar).
tabla_multiplicar = [[x * y for x in range(1, 6)] for y in range(1, 6)]
print(tabla_multiplicar)  # Resultado: [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], ...]

# Crear un diccionario con comprehensions.
numeros_cuadrados = {x: x**2 for x in range(5)}
print(numeros_cuadrados)  # Resultado: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Crear un conjunto (set) con comprehensions.
set_pares = {x for x in range(10) if x % 2 == 0}
print(set_pares)  # Resultado: {0, 2, 4, 6, 8}

# -----------------------------------------------------
# 2. DECORADORES
# -----------------------------------------------------
# Un decorador es una función que toma otra función como entrada,
# la modifica o extiende su funcionalidad, y devuelve la nueva función.

# Definir un decorador que mide el tiempo de ejecución de una función.
import time

def medir_tiempo(func):
    def envoltura(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos")
        return resultado
    return envoltura

# Decorar una función con @decorador.
@medir_tiempo
def sumar_lento(a, b):
    time.sleep(2)  # Simula un proceso lento.
    return a + b

# Llamar a la función decorada.
print(sumar_lento(3, 5))

# Decorador con parámetros: Personalizar el comportamiento del decorador.
def repetir(n):
    def decorador(func):
        def envoltura(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return envoltura
    return decorador

@repetir(3)
def saludar():
    print("Hola!")

# Llamar a la función decorada.
saludar()

# -----------------------------------------------------
# 3. GENERADORES
# -----------------------------------------------------
# Un generador es una función que produce una secuencia de valores de forma "perezosa" (on-demand)
# usando la palabra clave `yield`. Esto ahorra memoria y permite procesar datos grandes.

# Generador básico.
def generar_numeros(n):
    for i in range(n):
        yield i

# Usar el generador.
for numero in generar_numeros(5):
    print(numero)  # Resultado: 0, 1, 2, 3, 4

# Crear un generador en una sola línea con generator comprehensions.
gen_cuadrados = (x**2 for x in range(5))
print(next(gen_cuadrados))  # Resultado: 0
print(next(gen_cuadrados))  # Resultado: 1

# Generador infinito: Generar números pares infinitamente.
def generar_pares():
    n = 0
    while True:
        yield n
        n += 2

pares = generar_pares()
print(next(pares))  # Resultado: 0
print(next(pares))  # Resultado: 2

# Generador con múltiples yield: Producir valores diferentes según la condición.
def contador_personalizado(inicio, fin):
    while inicio < fin:
        yield f"Contando: {inicio}"
        inicio += 1
    yield "¡Terminado!"

for mensaje in contador_personalizado(1, 5):
    print(mensaje)

# -----------------------------------------------------
# 4. CUÁNDO USARLOS
# -----------------------------------------------------

# List Comprehensions:
# - Trabajar con listas de forma compacta y eficiente.
# - Ejemplo: Procesar datos rápidamente en una sola línea.

# Decoradores:
# - Añadir funcionalidad a funciones existentes sin modificar su código.
# - Ejemplo: Validar datos, medir rendimiento, añadir logs.

# Generadores:
# - Trabajar con datos grandes o infinitos sin cargar todo en memoria.
# - Ejemplo: Leer archivos línea por línea o procesar flujos de datos.

# -----------------------------------------------------
# ¡PRUEBA ESTOS EJEMPLOS Y DOMINA ESTAS HERRAMIENTAS ADICIONALES!
# -----------------------------------------------------
