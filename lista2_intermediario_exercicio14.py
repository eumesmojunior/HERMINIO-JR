total_ouro = 0

for bau in range(1, 6):
    moedas = int(input(f"Quantas moedas foram encontradas no baú {bau}? "))
    total_ouro = total_ouro + moedas

print("Riqueza acumulada:", total_ouro, "moedas")
