senha_secreta = "dragao123"
senha = ""

while senha != senha_secreta:
    senha = input("Digite a senha: ")

    if senha != senha_secreta:
        print("Senha incorreta, tente novamente!")

print("Cofre Aberto!")
