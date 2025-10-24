a = float(input("Digite o 1° lado"))
b = float(input("Digite o 2° lado"))
c = float(input("Digite o 3° lado"))
if a + b > c and a + c > b and b + c > a:
    print("Os lados formam um triângulo")

    if a == b == c:
        print("Triângulo equilátero")
    elif a == b or a == c or b == c:
    print("Triângulo Isóceles")
    else:
    print("Triangulo Escaleno")
else:
    print("Os lados NÃO formam um triângulo.")
