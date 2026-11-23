ano = int(input("Digite um ano: "))

if ano < 1500:
    print("Você encontrou dinossauros ou cavaleiros!")
elif ano < 2000:
    print("Você está no século passado!")
elif ano == 2026:
    print("Você está no presente!")
else:
    print("Você está no futuro com os carros voadores!")
    