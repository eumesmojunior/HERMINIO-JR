idade = int(input("Digite sua idade: "))

if idade >= 14:
    print("Bem-vindo à equipe avançada!")
else:
    faltam = 14 - idade
    print(f"Faltam {faltam} anos para você entrar na equipe avançada!")