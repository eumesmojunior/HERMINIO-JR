numero = int(input("Digite um número inteiro: "))

divisores = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        divisores = divisores + 1

if divisores == 2:
    print("É um Número Primo!")
else:
    print("Não é um Número Primo.")
    