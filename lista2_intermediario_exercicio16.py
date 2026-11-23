energia = 100

while energia > 0:
    acao = input("Você quer correr ou pular? ")

    if acao == "correr":
        energia = energia - 20
    elif acao == "pular":
        energia = energia - 15
    else:
        print("Ação inválida.")
        continue

    print("Energia restante:", energia)

print("O herói desmaiou de cansaço!")