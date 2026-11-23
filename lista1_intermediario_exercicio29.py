vida = 100

resposta = int(input("Quanto é 15 x 3? "))

if resposta == 45:
    print("Você ganhou o tesouro!")
else:
    vida = vida - 50
    print("Resposta errada!")
    print("Vida restante:", vida)
    