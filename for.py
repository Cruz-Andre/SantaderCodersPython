#aqui vamos de 0 até 9
for variavel in range(10):
    print(variavel)

print("-----------------------")

#aqui vamos de 1 até 5 ou do 1 até o numero menor que 6
for variavel in range(1, 6):
    print(variavel)

print("-----------------------")

#aqui vamos de 1 até 11 mas pulando de 3 em 3
for variavel in range(1, 12, 3):
    print(variavel)

print("-----------------------")

"""
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3  = float(input("Digite a terceira nota: "))
"""

soma = 0
for i in range(1, 4):
    nota = float(input(f"Digite a sua nota {i}: ")) #o f antes da string serve injetar o valor da variavel i na string
    soma = soma + nota

print(soma / 3)
