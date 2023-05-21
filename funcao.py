# Funções

# 1. O que são funções e por que utilizá-las?

# Funções que já utilizamos anteriormente...
"""
 print() - Imprime uma mensagem (int, float, str) no console (terminal, cmd)
 input() - Retorna um dado informado pelo usuário (entrada padrão) e pode receber uma string
 len() - Recebe uma lista e retorna o tamanho da lista
 max() - Retorna o maior número de uma lista
"""
# 2. Criação de funções

# Função inicial
def saudacao():
    print('Olá, seja bem-vindo(a)!')
    print('Vamos começar?')

saudacao()

print("-----------------------------------------------------")

# Função com parâmetros
def saudacao2(nome, curso):
    print(f'Olá, seja bem-vindo(a), {nome}!')
    print(f'Vamos começar o curso de {curso}!')

saudacao2("André",  "Python")
saudacao2("Pafuncio",  "JavaScript")

print("-----------------------------------------------------")

# Função com parâmetros default
def saudacao3(nome, curso = "Python"):
    print(f'Olá, seja bem-vindo(a), {nome}!')
    print(f'Vamos começar o curso de {curso}!')

saudacao3("André", "C++")
saudacao3("Pafuncio")

print("-----------------------------------------------------")

# Funções com retorno
def soma(num1, num2):
    return num1 + num2

resultado = soma(5, 7)
print('O Resultado da soma é:', resultado)

print("-----------------------------------------------------")

def calculadora(num1, num2, operacao = '+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        return num1 / num2
    else:
        return 'Operação inválida'

resultado = calculadora(10, 20, '*')
print('O resultado da calculadora é:', resultado)