distancia = input("Prefere atacar de longe (1) ou de perto (2)? ")

if distancia == "1":
    escolha = input("Magia (A) ou Arco (B)? ")

    if escolha == "A":
        print("Sua classe é Mago!")
    elif escolha == "B":
        print("Sua classe é Arqueiro!")
    else:
        print("Opção inválida.")

elif distancia == "2":
    escolha = input("Espada (A) ou Adagas (B)? ")

    if escolha == "A":
        print("Sua classe é Guerreiro!")
    elif escolha == "B":
        print("Sua classe é Assassino!")
    else:
        print("Opção inválida.")

else:
    print("Opção inválida.")
    