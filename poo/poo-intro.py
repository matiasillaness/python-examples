# -----------------------------------------------------
# 1. INTRODUCCIÓN A LA POO
# -----------------------------------------------------
# La Programación Orientada a Objetos (POO) se basa en 4 pilares:
# - Encapsulamiento: Proteger los datos y funciones.
# - Abstracción: Ocultar detalles internos, mostrando solo lo necesario.
# - Herencia: Reutilizar código mediante clases derivadas.
# - Polimorfismo: Métodos con el mismo nombre que se comportan diferente según el contexto.

# -----------------------------------------------------
# 2. CLASES Y OBJETOS
# -----------------------------------------------------
# Una clase es un modelo que define propiedades (atributos) y comportamientos (métodos).
# Un objeto es una instancia de una clase.

# Definir una clase
class Persona:
    # Constructor: Define atributos iniciales
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo público
        self.edad = edad

    # Método: Comportamiento de la clase
    def saludar(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."

# Crear un objeto
persona1 = Persona("Matías", 20)
print(persona1.saludar())  # Llamar al método

# Acceder y modificar atributos
print(persona1.nombre)  # Acceder al atributo
persona1.nombre = "Lucas"
print(persona1.saludar())

# -----------------------------------------------------
# 3. ENCAPSULAMIENTO
# -----------------------------------------------------
# Controlar el acceso a los atributos con niveles de visibilidad:
# - Público: Atributos y métodos accesibles desde cualquier lugar.
# - Privado: Se usa un guion bajo (_) o doble (__).

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado

    def mostrar_saldo(self):
        return f"Saldo disponible: {self.__saldo}."

    def depositar(self, monto):
        self.__saldo += monto

    def retirar(self, monto):
        if monto > self.__saldo:
            return "Fondos insuficientes."
        self.__saldo -= monto
        return "Retiro exitoso."

# Uso de la clase
cuenta = CuentaBancaria("Matías", 5000)
print(cuenta.mostrar_saldo())
cuenta.depositar(1000)
print(cuenta.mostrar_saldo())
print(cuenta.retirar(7000))

# -----------------------------------------------------
# 4. HERENCIA
# -----------------------------------------------------
# Una clase hija puede heredar atributos y métodos de una clase padre.

class Empleado(Persona):  # Clase Empleado hereda de Persona
    def __init__(self, nombre, edad, puesto):
        super().__init__(nombre, edad)  # Llama al constructor de la clase padre
        self.puesto = puesto

    def presentarse(self):
        return f"{self.saludar()} Trabajo como {self.puesto}."

# Crear un objeto de la clase hija
empleado1 = Empleado("Ana", 28, "Desarrolladora")
print(empleado1.presentarse())

# -----------------------------------------------------
# 5. POLIMORFISMO
# -----------------------------------------------------
# Métodos con el mismo nombre, pero comportamiento diferente en cada clase.

class Animal:
    def hacer_sonido(self):
        raise NotImplementedError("Este método debe implementarse en una subclase.")

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"

# Uso de polimorfismo
animales = [Perro(), Gato()]
for animal in animales:
    print(animal.hacer_sonido())

# -----------------------------------------------------
# 6. ABSTRACCIÓN
# -----------------------------------------------------
# Usar clases abstractas para definir interfaces comunes.

from abc import ABC, abstractmethod

class Figura(ABC):  # Clase abstracta
    @abstractmethod
    def area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio ** 2

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

# Crear objetos
circulo = Circulo(5)
rectangulo = Rectangulo(4, 6)

# Calcular áreas
print(f"Área del círculo: {circulo.area()}")
print(f"Área del rectángulo: {rectangulo.area()}")

# -----------------------------------------------------
# 7. MÉTODOS Y ATRIBUTOS DE CLASE
# -----------------------------------------------------

class MiClase:
    contador = 0  # Atributo de clase (compartido por todas las instancias)

    def __init__(self, valor):
        self.valor = valor  # Atributo de instancia
        MiClase.contador += 1

    @classmethod
    def mostrar_contador(cls):
        return f"Instancias creadas: {cls.contador}"

# Crear objetos
obj1 = MiClase(10)
obj2 = MiClase(20)

# Mostrar el contador de instancias
print(MiClase.mostrar_contador())

# -----------------------------------------------------
# 8. MÉTODOS ESTÁTICOS
# -----------------------------------------------------
# Métodos que no dependen de la instancia ni de la clase.

class Calculadora:
    @staticmethod
    def sumar(a, b):
        return a + b

    @staticmethod
    def restar(a, b):
        return a - b

# Usar métodos estáticos
print(Calculadora.sumar(5, 3))
print(Calculadora.restar(10, 4))

# -----------------------------------------------------
# ¡PRUEBA ESTOS EJEMPLOS PARA ENTENDER POO EN PYTHON!
# -----------------------------------------------------
