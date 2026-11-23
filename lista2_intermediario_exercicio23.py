numero_secreto = 42
tentativas = 0
chute = 0

while chute != numero_secreto:
    chute = int(input("Adivinhe o número secreto: "))
    tentativas = tentativas + 1

    if chute > numero_secreto:
        print("Chutou alto! Tente um menor.")
    elif chute < numero_secreto:
        print("Chutou baixo! Tente um maior.")
    else:
        print("Você acertou!")

print("Número de tentativas:", tentativas)