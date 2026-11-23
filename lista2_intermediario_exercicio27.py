andar_atual = 0

while True:
    destino = int(input("Digite o andar desejado (0 a 10) ou -1 para sair: "))

    if destino == -1:
        print("Elevador encerrado.")
        break

    if destino < 0 or destino > 10:
        print("Andar inválido.")
        continue

    if destino > andar_atual:
        for andar in range(andar_atual + 1, destino + 1):
            print("Passando pelo andar", andar)

    elif destino < andar_atual:
        for andar in range(andar_atual - 1, destino - 1, -1):
            print("Passando pelo andar", andar)

    else:
        print("Você já está nesse andar.")

    andar_atual = destino
    print("Chegou ao andar", andar_atual)