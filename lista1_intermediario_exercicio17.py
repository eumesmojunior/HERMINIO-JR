print("1 - Poção de Vida - 20 moedas")
print("2 - Poção de Mana - 30 moedas")
print("3 - Poção de Força - 50 moedas")

opcao = int(input("Escolha uma poção (1, 2 ou 3): "))

if opcao == 1:
    preco = 20
    print("Você comprou uma Poção de Vida.")
elif opcao == 2:
    preco = 30
    print("Você comprou uma Poção de Mana.")
elif opcao == 3:
    preco = 50
    print("Você comprou uma Poção de Força.")
else:
    preco = 0
    print("Opção inválida.")

print("Valor da compra:", preco, "moedas")