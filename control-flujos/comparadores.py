# Comparador de igualdad (==)
print(5 == 5)  # True, porque 5 es igual a 5
print(5 == 3)  # False, porque 5 no es igual a 3

# Comparador de desigualdad (!=)
print(5 != 3)  # True, porque 5 no es igual a 3
print(5 != 5)  # False, porque 5 es igual a 5

# Comparador mayor que (>)
print(5 > 3)   # True, porque 5 es mayor que 3
print(3 > 5)   # False, porque 3 no es mayor que 5

# Comparador menor que (<)
print(3 < 5)   # True, porque 3 es menor que 5
print(5 < 3)   # False, porque 5 no es menor que 3

# Comparador mayor o igual que (>=)
print(5 >= 3)  # True, porque 5 es mayor o igual a 3
print(3 >= 5)  # False, porque 3 no es mayor ni igual a 5
print(5 >= 5)  # True, porque 5 es igual a 5

# Comparador menor o igual que (<=)
print(3 <= 5)  # True, porque 3 es menor o igual a 5
print(5 <= 3)  # False, porque 5 no es menor ni igual a 3
print(5 <= 5)  # True, porque 5 es igual a 5

# Comparador de identidad (is)
a = [1, 2, 3]
b = a
print(a is b)  # True, porque 'a' y 'b' son el mismo objeto en memoria

c = [1, 2, 3]
print(a is c)  # False, porque 'a' y 'c' son diferentes objetos aunque tengan el mismo valor

# Comparador de no identidad (is not)
print(a is not b)  # False, porque 'a' y 'b' son el mismo objeto
print(a is not c)  # True, porque 'a' y 'c' son diferentes objetos
