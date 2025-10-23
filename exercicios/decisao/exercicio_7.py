numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))
numero3 = float(input("Digite o terceiro numero: "))

maior = numero1
menor = numero1

if numero2 > maior:
    maior = numero2
if numero3 > maior:
    maior = numero3

if numero2 < menor:
    menor = numero2
    if numero3 > menor:
        menor = numero3

print("O maior numero é:", maior)
print("O menor numero é:", menor)

