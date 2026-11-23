tesouro = float(input("Digite o valor do tesouro: "))

if tesouro > 1000:
    imposto = tesouro * 0.10
    valor_final = tesouro - imposto

    print(f"Imposto cobrado: {imposto:.2f} moedas")
    print(f"Tesouro após o imposto: {valor_final:.2f} moedas")
else:
    print("Você não paga imposto.")
    