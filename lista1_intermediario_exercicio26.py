velocidade = float(input("Digite a velocidade do carro: "))

if velocidade <= 80:
    print("Siga em paz")
elif velocidade <= 100:
    print("Multa leve de 50 moedas")
else:
    print("Multa gravíssima de 200 moedas e carro apreendido!")
    