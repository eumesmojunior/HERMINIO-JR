total = 0

while True:
    preco = float(input("Digite o preço do produto (0 para finalizar): R$ "))

    if preco == 0:
        break

    total = total + preco

print(f"Valor total da compra: R$ {total:.2f}")
