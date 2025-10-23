valor_hora = float(input("Digite o valor da sua hora: "))
horas = float(input("Digite o total de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas

if salario_bruto <= 900:
    ir = 0
elif salario_bruto <= 1500:
    ir = salario_bruto * 0.05
elif salario_bruto <= 2500:
    ir = salario_bruto * 0.10
else:
    ir = salario_bruto * 0.20

inss = salario_bruto * 0.10
fgts = salario_bruto * 0.11
sindicato = salario_bruto * 0.03

total_descontos = ir + inss + sindicato
salario_liquido = salario_bruto -total_descontos

print("Salário Bruto: R$", salario_bruto)
print("(-) IR: R$", ir)
print("(-) INSS: R$", inss)
print("(-) Sindicato: R$", sindicato)
print("FGTS (não descontado): R$", fgts)
print("Total de descontos: R$", total_descontos)
print("Salário liquido: R$", salario_liquido)