class operaciones:
    def op1(suma, x):
        return suma + x
    def op2(x, y):
        return x + (y ** 2)
    def op3(suma, x, y):
        return suma + (x / y)
    
suma = 0
x = 20
y = 40

suma = operaciones.op1(suma, x)
x = operaciones.op2(x, y)
suma = operaciones.op3(suma, x, y)
print(f"el valor de la suma es: {suma}")