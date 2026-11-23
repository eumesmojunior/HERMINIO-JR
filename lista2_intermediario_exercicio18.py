palavra = input("Digite uma palavra: ")

contador_a = 0

for letra in palavra:
    print(letra)

    if letra == "a":
        contador_a = contador_a + 1

print("Quantidade de letras a:", contador_a)
