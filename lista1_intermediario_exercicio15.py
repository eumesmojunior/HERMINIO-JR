senha = input("Digite a senha secreta: ")

if senha == "dragao":
    print("Senha correta!")
elif senha == "DRAGAO":
    print("Quase! Mas você gritou a senha (Caps Lock). Tente minúsculas.")
else:
    print("Senha incorreta.")
    