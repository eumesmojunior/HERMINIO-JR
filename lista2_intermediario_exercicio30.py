fichas = 5

while True:
    print("\n--- FLIPERAMA ---")
    print("Fichas disponíveis:", fichas)
    print("1 - Jogar Corrida (1 ficha)")
    print("2 - Jogar Luta (2 fichas)")
    print("3 - Comprar mais fichas")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        if fichas >= 1:
            fichas = fichas - 1

            for fase in range(1, 4):
                print(f"Jogando... Fase {fase}...")

        else:
            print("Você não tem fichas suficientes.")

    elif opcao == "2":
        if fichas >= 2:
            fichas = fichas - 2

            for fase in range(1, 4):
                print(f"Jogando... Fase {fase}...")

        else:
            print("Você não tem fichas suficientes.")

    elif opcao == "3":
        quantidade = int(input("Quantas fichas deseja comprar? "))
        fichas = fichas + quantidade
        print("Fichas compradas com sucesso!")

    elif opcao == "4":
        print("Obrigado por jogar!")
        break

    else:
        print("Opção inválida.")

    if fichas == 0:
        resposta = input("Suas fichas acabaram. Deseja comprar mais? (sim/não): ")

        if resposta == "não":
            print("Fim de jogo!")
            break
        