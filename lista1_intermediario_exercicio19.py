mesada = float(input("Digite o valor da mesada: "))
nota_a = input("Você tirou nota A em matemática? (sim/não): ")

if nota_a == "sim":
    mesada = mesada + 20

print(f"Total final da mesada: {mesada:.2f} moedas")