vida_heroi = 100
vida_goblin = 80

while vida_heroi > 0 and vida_goblin > 0:
    print("\n1 - Atacar")
    print("2 - Curar")

    opcao = input("Escolha uma ação: ")

    if opcao == "1":
        vida_goblin = vida_goblin - 15
        print("Você atacou o Goblin!")

    elif opcao == "2":
        vida_heroi = vida_heroi + 10
        print("Você recuperou 10 de vida!")

    else:
        print("Opção inválida.")
        continue

    if vida_goblin > 0:
        vida_heroi = vida_heroi - 12
        print("O Goblin contra-atacou!")

    print("Vida do Herói:", vida_heroi)
    print("Vida do Goblin:", vida_goblin)

if vida_heroi > 0:
    print("O Herói venceu!")
else:
    print("O Goblin venceu!")
    