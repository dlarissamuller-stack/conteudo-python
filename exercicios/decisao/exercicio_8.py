produto1 = float(input("Preço do primeiro produto: "))
produto2 = float(input("Preço do segundo produto: "))
produto3 = float(input("Preço do terceiro produto: "))

if produto1 < produto2 and produto1 < produto3:
    print("Compre o primeiro produto")
elif produto2 < produto3:
    print("Compre o segundo produto")
else:
    print("Compre o terceiro produto")