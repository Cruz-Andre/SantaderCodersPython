# listas

# Antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# com lista
notas = [7.9, 9.7, 8.2]

# Criando listas
lista = []
lista = list() # outra forma de criar uma lista
lista = [26, 'André', 3.14, True]
listaDeListas = [10, [1, 2, 3]]

# Indexação e Slices (fatiamento)
lista = [26, 'André', 3.14, True]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print("--------------------------------------")
print(lista[-1]) # Último elemento
print(lista[-2]) # Elemento anterior ao Último

print("--------------------------------------")
#slices
lista = [10, 50, 30, 40, 25, 60, 5]

print(lista[0:3]) # 0 até 2 (sem incluir o 3)
print(lista[3:6]) # 3 até 5 (sem incluir o 6)
print(lista[3:]) # 3 até o final
print(lista[2:6:2]) # de 2 em 2 até o 6 (sem incluir o 6)
print(lista[:]) # 0 até o final
print(lista[::]) # 0 até o final

print("--------------------------------------")
# Interações com FOR

# 1. Utilizando os próprios elementos da lista
for elemento in lista:
    print(elemento)

print("--------------------------------------")

# 2. Utilizando índices
print('Comprimento da lista:', len(lista))

for i in range(len(lista)):
    print(lista[i])

print("--------------------------------------")

# Métodos de listas

lista = [1, 3, 12, 8, 2]

# append
print(lista)
lista.append(3)
print(lista)

print("--------------------------------------")

# insert
lista.insert(2, 10)
print(lista)

print("--------------------------------------")

# extend
lista2 = [1, 2, 3]
lista.extend(lista2)
print(lista)

print("--------------------------------------")

# pop
lista.pop() # remove o Último elemento
print('lista após o pop():', lista)

lista.pop(0) # remove o elemento de índice 0
print('lista após o pop(0):', lista)

print("--------------------------------------")

# remove
lista.remove(3) # remove o primeiro elemento 3 que encontrar
print('lista após o remove(3):', lista)

print("--------------------------------------")

# count
print('Quantidade de elementos 2 na lista:', lista.count(2))

print("--------------------------------------")

# index
print('Índice do elemento 12:', lista.index(12))

print("--------------------------------------")

# sort
lista.sort() # ordena a lista de forma crescente
print(lista)
lista.sort(reverse=True) # ordena a lista de forma decrescente
print(lista)

print("--------------------------------------")

# Funções para listas

# len
print('Tamanho da lista:', len(lista))

print("--------------------------------------")

# sum
print('Soma dos elementos da lista:', sum(lista))

print("--------------------------------------")

# max
print('Maior elemento da lista:', max(lista))

print("--------------------------------------")

# min
print('Menor elemento da lista:', min(lista))