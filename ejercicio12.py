class calculo:
    def salariobruto(horas_trabajadas, valor_hora):
        return (horas_trabajadas * valor_hora)
    def retefuente(porcentaje_retefuente, salario_bruto):
        return (porcentaje_retefuente * salario_bruto)
    def salarioneto(salario_bruto, retencion_fuente):
        return (salario_bruto - retencion_fuente)

horas_trabajadas = 48
valor_hora = 5000
porcentaje_retefuente = 12.5/100

salario_bruto = calculo.salariobruto(horas_trabajadas, valor_hora)
retencion_fuente = calculo.retefuente(porcentaje_retefuente, salario_bruto)
salario_neto = calculo.salarioneto(salario_bruto, retencion_fuente)

print(f"El salario bruto es: {salario_bruto}")
print(f"La retencion de la fuente es: {retencion_fuente}")
print(f"El salario neto es: {salario_neto}")

