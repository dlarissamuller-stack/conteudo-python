saque = int(input("Digite o valor a ser sacado (entre 10 e 600): "))

if saque < 10 or saque > 600:
    print("Não é possível sacar o valor informado!")
    exit(1)

    qtd_cen= 0
    qtd_cinquenta = 0
    qtd_dez = 0
    qtd_cinco = 0
    qtd_um = 0

if saque >= 100:
    qtd_cen = saque // 100
    saque = saque - (qtd_cen * 100)

    qtd_cinquenta = saque // 50
    saque = saque - (qtd_cinquenta * 50)

    qtd_dez = saque // 10
    saque = saque - (qtd_dez * 10)

    qtd_cinco = saque // 5
    saque = saque - (qtd_cinco * 5)

    qtd_um = saque

    print("Notas de 100:", qtd_cen)
    print("Notas de 50:", qtd_cinquenta)
    print("Notas de 10:", qtd_dez)
    print("Notas de 5:", qtd_cinco)
    print("Notas de 1:", qtd_um)