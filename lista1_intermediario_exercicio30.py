senha = input("Digite a senha secreta para entrar na Taverna: ")

if senha == "dragao123":
    print("Entrada liberada!")

    idade = int(input("Digite sua idade: "))

    if idade < 13:
        bebida = "Suco de Uva"
    else:
        bebida = "Poção Mágica"

    print("Você recebeu:", bebida)

    print("\nEscolha sua personalidade:")
    print("1 - Corajoso")
    print("2 - Inteligente")
    print("3 - Misterioso")

    personalidade = input("Escolha 1, 2 ou 3: ")

    if personalidade == "1":
        item = "Espada"
        preco = 50
    elif personalidade == "2":
        item = "Livro de Magia"
        preco = 40
    elif personalidade == "3":
        item = "Amuleto"
        preco = 30
    else:
        item = ""
        preco = 0
        print("Opção inválida.")

    if preco > 0:
        ouro = float(input("Quantas moedas de ouro você tem? "))

        print(f"O item escolhido foi {item}, que custa {preco} moedas.")

        if ouro >= preco:
            troco = ouro - preco
            print("Compra realizada!")
            print(f"Troco: {troco:.2f} moedas.")
        else:
            falta = preco - ouro
            print("Você não tem ouro suficiente.")
            print(f"Faltam {falta:.2f} moedas.")

else:
    print("Senha incorreta. Entrada negada.")
    