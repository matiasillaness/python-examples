# Definimos una variable x
x = 8

# Estructura if-else con elif
if x > 10:  # Si x es mayor que 10
    print("x es mayor que 10")
elif x > 5:  # Si x no es mayor que 10, pero es mayor que 5
    print("x es mayor que 5 pero menor o igual a 10")
else:  # Si x es 5 o menor
    print("x es 5 o menor")

# Otro ejemplo con una condición diferente
x = 3

if x > 10:
    print("x es mayor que 10")
elif x > 5:
    print("x es mayor que 5 pero menor o igual a 10")
else:
    print("x es 5 o menor")  # Esta es la opción que se ejecutará



t = 10

# Usando operador ternario
resultado = "x es mayor que 5" if x > 5 else "x es 5 o menor"
print(resultado)

