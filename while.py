numeroSorteado = 15

numeroEscolhido = int(input("Informe um número entre 1 e 20: "))

while numeroEscolhido != numeroSorteado:
    print('Você errou o número, tente novamente...')
    numeroEscolhido = int(input("Informe um número entre 1 e 20: "))

print('Parabéns, você acertou o número sorteado')


# exemplo 2 estrutura com contador
contador = 0

while contador < 5:
    print(contador)
    contador = contador + 1