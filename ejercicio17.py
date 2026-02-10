import math
class calculo:
    def area(radio):
        return math.pi * (radio ** 2) 
    def longitud(radio):
        return 2 * (math.pi * radio)

radio = float(input("Ingrese el radio del circulo: "))
area = calculo.area(radio)
longitud = calculo.longitud(radio)

print(f"El area del circulo es: {round(area, 2)} \nY su longitud es: {round(longitud, 2)}")
