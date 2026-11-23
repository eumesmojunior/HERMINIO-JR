saldo = 100

meses = int(input("Quantos meses o dinheiro ficará no banco? "))

for mes in range(1, meses + 1):
    saldo = saldo * 1.10
    print(f"Mês {mes}: {saldo:.2f} moedas")
    