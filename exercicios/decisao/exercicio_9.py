numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))
numero3 = float(input("Digite o terceiro numero: "))

if numero1 > numero2 and numero1 > numero3:
    if numero2 > numero3:
        print(numero1, numero2, numero3)
    else:
        print(numero1, numero3, numero2)
elif numero2 > numero1 and numero2 > numero3:
    if numero1 > numero3:
        print(numero2, numero1, numero3)
    else:
        print(numero2, numero3, numero1)
else:
    if numero1 > numero2:
        print(numero3, numero1, numero2)
    else:
        print(numero3, numero2, numero1)