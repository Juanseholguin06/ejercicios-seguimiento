import math
class calculos: 
    def cuadrado(numero):
        return numero ** 2
    def cubo(numero):
        return numero ** 3

numero = float(input("Ingresa un numero: "))

cuadrado = calculos.cuadrado(numero)
cubo = calculos.cubo(numero)

print(f"El cuadrado del numero ingresado es {cuadrado} y su cubo es {cubo}")