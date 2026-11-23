mesada = float(input("Quanto você tem guardado? R$ "))
preco_jogo = float(input("Qual o preço do jogo? R$ "))

if mesada >= preco_jogo:
    troco = mesada - preco_jogo
    print(f"Você pode comprar o jogo. Troco: R$ {troco:.2f}")
else:
    falta = preco_jogo - mesada
    print(f"Faltam R$ {falta:.2f} para comprar o jogo.")
    