inventario = []

while True:
    item = input("Digite um item para adicionar ao inventário ou 'sair' para encerrar: ")

    if item == "sair":
        break

    inventario.append(item)

print("Inventário:", inventario)