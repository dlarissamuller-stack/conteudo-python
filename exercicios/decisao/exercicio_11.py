salario = float(input("Digite o salário do colaborador: "))

if salario <= 1450:
    aumento = 0.20
elif salario <=2800:
    aumento = 0.15
elif salario <= 3500:
    aumento = 0.10
else:
    aumento = 0.05

valor_aumento = salario * aumento
novo_salario = salario + valor_aumento

print("Salário antes do reajuste: R$", salario)
print("Percentual de aumento: ", aumento * 100, "%")
print("Valor do aumento: R$", valor_aumento)
print("Novo salário após o aumento: R$", novo_salario)