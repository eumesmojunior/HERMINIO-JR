# Primeiro exemplo: o input() recebe a idade como texto.

idade = input("Digite sua idade: ")

# Se tentarmos fazer idade + 1, o Python dará erro.
# Isso acontece porque input() recebe o valor como texto (string),
# e não é possível somar diretamente um texto com um número inteiro.

# idade + 1

# Forma correta:
# precisamos converter a idade para número inteiro usando int().

idade = int(input("Digite sua idade novamente: "))

print("No próximo ano você terá:", idade + 1)