# 10. Funciones del módulo math
import math

# 10.1 ceil(x): Devuelve el menor entero mayor o igual que x.
print(math.ceil(4.2))  # Resultado: 5

# 10.2 floor(x): Devuelve el mayor entero menor o igual que x.
print(math.floor(4.7))  # Resultado: 4

# 10.3 fabs(x): Devuelve el valor absoluto de x como un número flotante.
print(math.fabs(-5))  # Resultado: 5.0

# 10.4 factorial(x): Devuelve el factorial de x (x debe ser un entero no negativo).
print(math.factorial(5))  # Resultado: 120

# 10.5 sqrt(x): Devuelve la raíz cuadrada de x.
print(math.sqrt(16))  # Resultado: 4.0

# 10.6 pow(x, y): Devuelve x elevado a la potencia y.
print(math.pow(2, 3))  # Resultado: 8.0

# 10.7 log(x, base): Devuelve el logaritmo de x en la base especificada.
print(math.log(8, 2))  # Resultado: 3.0

# 10.8 sin(x), cos(x), tan(x): Devuelven el seno, coseno y tangente de x (en radianes).
print(math.sin(math.pi / 2))  # Resultado: 1.0
print(math.cos(math.pi))  # Resultado: -1.0
print(math.tan(math.pi / 4))  # Resultado: 1.0

# 10.9 degrees(x): Convierte radianes a grados.
print(math.degrees(math.pi))  # Resultado: 180.0

# 10.10 radians(x): Convierte grados a radianes.
print(math.radians(180))  # Resultado: 3.14159...

# 10.11 gcd(x, y): Devuelve el máximo común divisor de x e y.
print(math.gcd(48, 18))  # Resultado: 6
