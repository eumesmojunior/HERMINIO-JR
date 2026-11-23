senha_secreta = "dragao123"
tentativas = 0

while tentativas < 3:
    senha = input("Digite a senha: ")

    if senha == senha_secreta:
        print("Cofre Aberto!")
        break
    else:
        tentativas = tentativas + 1
        print("Senha incorreta.")

if tentativas == 3:
    print("Cartão Bloqueado! Chamando os guardas!")
    