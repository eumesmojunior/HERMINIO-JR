dinheiro = float(input("Quanto dinheiro você tem? R$ "))

print("1 - Lanche - R$ 15")
print("2 - Suco - R$ 8")
print("3 - Combo - R$ 20")

opcao = int(input("Escolha uma opção: "))

if opcao == 1:
    preco = 15
elif opcao == 2:
    preco = 8
elif opcao == 3:
    preco = 20
else:
    preco = 0
    print("Opção inválida.")

if preco > 0:
    if dinheiro >= preco:
        print("Compra liberada!")
    else:
        print("Compra negada. Dinheiro insuficiente.")