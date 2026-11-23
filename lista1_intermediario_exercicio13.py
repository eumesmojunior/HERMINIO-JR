senha = input("Digite a senha: ")

if senha == "dragao":
    pin = input("Digite o PIN de 4 números: ")

    if pin == "1234":
        print("Acesso ao Cofre Liberado")
    else:
        print("PIN incorreto")
else:
    print("Senha incorreta")
    