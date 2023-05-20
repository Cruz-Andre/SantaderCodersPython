# variáveis
"""
Tipos de variáveis:
1. int: números inteiros
2. float: números com ponto flutuante (decimais)
3. str: texto (strings)
4. bool: valores lógicos (booleano): True ou False
"""

idade = 40 # criando uma variável int (inteiro)
altura = 1.81 # criando uma variável float (decimais)
nome = "André Cruz" # criando uma variável str (texto)
estudando = True # criando uma variável bool (booleano)

print(type(idade)) # imprimindo o tipo da variável idade
print(type(altura)) # imprimindo o tipo da variável altura
print(type(nome)) # imprimindo o tipo da variável nome
print(type(estudando)) # imprimindo o tipo da variável estudando


# Obtendo dados do usuário e salvando em variáveis
linguagem = input('Qual é a linguagem de programação que vocé está estudando? ')
print('A linguagem que vocé está estudando é', linguagem + '!')
