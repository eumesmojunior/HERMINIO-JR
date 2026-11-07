dano_base = 20
tem_escudo = True

if tem_escudo:
    dano_recebido = dano_base * 0.5
else:
    dano_recebido = dano_base

print("Dano recebido:", dano_recebido)