# Bucle FOR: Itera sobre una secuencia (lista, rango, cadena, etc.)
# Ejemplo 1: Usando un rango de números
for i in range(5):  # range(5) genera los números 0, 1, 2, 3, 4
    print(f"Valor de i: {i}")  # Imprime cada valor de i

# Ejemplo 2: Iterando sobre una lista
frutas = ["manzana", "pera", "uva"]
for fruta in frutas:
    print(f"Fruta actual: {fruta}")  # Imprime cada elemento de la lista

# Ejemplo 3: Iterando sobre una cadena
palabra = "Python"
for letra in palabra:
    print(f"Letra: {letra}")  # Imprime cada carácter de la cadena

# Ejemplo 4: Usando break y continue
for num in range(10):
    if num == 5:
        print("Se encontró el número 5, saliendo del bucle...")
        break  # Termina el bucle si el número es 5
    if num % 2 == 0:
        continue  # Salta al siguiente ciclo si el número es par
    print(f"Número impar: {num}")  # Solo se imprimen números impares hasta 5

# -----------------------------------------------------

# Bucle WHILE: Se ejecuta mientras una condición sea verdadera
# Ejemplo 1: Contador simple
contador = 0
while contador < 5:  # Mientras el contador sea menor a 5
    print(f"Contador: {contador}")
    contador += 1  # Incrementa el contador

# Ejemplo 2: Condición dinámica
x = 10
while x > 0:
    print(f"x vale: {x}")
    x -= 2  # Decrementa x en 2 en cada iteración

# Ejemplo 3: Uso de break y continue
x = 10
while x > 0:
    x -= 1
    if x == 5:
        print("Encontramos 5, saliendo del bucle...")
        break  # Sale del bucle si x es 5
    if x % 2 == 0:
        continue  # Salta el resto del bloque si x es par
    print(f"x impar: {x}")  # Solo imprime si x es impar

# -----------------------------------------------------

# Bucle anidado (FOR dentro de FOR)
# Ejemplo: Tablas de multiplicar
for i in range(1, 4):  # Ciclo externo: Números del 1 al 3
    for j in range(1, 4):  # Ciclo interno: Números del 1 al 3
        print(f"{i} x {j} = {i * j}")  # Calcula y muestra la multiplicación
    print("---")  # Separador para cada tabla
