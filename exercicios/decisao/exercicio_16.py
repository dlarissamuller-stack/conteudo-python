import math
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if a == 0:
    print("Não é equação de 2° grau!")
    exit(1)

delta = b ** 2 - 4 * a * c

if delta < 0:
        print("Delta", delta)
        print("Não é possivel calcular raíz de números negativos")

if delta == 0:
        x = (b * -1) / (2*a)
        print(f"O valor de x é {x}")
else:
    raiz = math.sqrt(delta)
    xa = (b * -1) + raiz / (2 * a)
    xb = (b * -1) - raiz / (2 * a)
    print(f"o valor de x' é {xa}")
    print(f"o valor de x' é {xb}")
