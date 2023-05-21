# Dicionários

# Criando dicionários
dicionario = {}
dicionario = dict() #outra forma de criar um dicionário
dicionario = {'nome': 'André', 'idade': 42, 'altura': 1.81}

# Acessando os valores
print(dicionario)
print(dicionario['idade'])

print("--------------------------------------------------------------------")

# Adicionando elementos em um dicionário
dicionario['programador'] = True
print(dicionario)

dicionario['altura'] = 1.79 # Alterando um valor
print(dicionario)

print("--------------------------------------------------------------------")

# Interando sobre um dicionário
for chave in dicionario: # Iterando sobre as chaves
    print(chave) # Imprimindo as chaves

print("\n")

for chave in dicionario:
    print(chave, dicionario[chave]) # Imprimindo as chaves e valores

print("--------------------------------------------------------------------")

# Testando a existência de uma chave
print('peso' in dicionario) # False
print('altura' in dicionario) # True