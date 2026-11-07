melhor_tempo = None
vencedor = ""

for ciclista in range(1, 6):
    tempo = float(input(f"Digite o tempo do ciclista {ciclista}: "))

    if melhor_tempo is None or tempo < melhor_tempo:
        melhor_tempo = tempo
        vencedor = f"Ciclista {ciclista}"

print("Vencedor:", vencedor)
print("Melhor tempo:", melhor_tempo)