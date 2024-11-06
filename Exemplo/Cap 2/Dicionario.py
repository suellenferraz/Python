# Dicionario é uma coleção de dados que contém chave e valor associado a ela.
# Dicionario é representado por {} e os elementos são separados por vírgula.
# Dicionario é mutável, ou seja, pode ser alterado.

# Exemplo 1
# Criando um dicionário
dicionario = {'nome': 'João', 'idade': 25, 'cidade': 'São Paulo'}
print(dicionario)

# Exemplo 2
# Acessando elementos do dicionário
print(dicionario['nome'])
print(dicionario['idade'])
print(dicionario['cidade'])

# Exemplo 3
# Alterando elementos do dicionário
dicionario['nome'] = 'Maria'
print(dicionario)

# Exemplo 4
# Adicionando elementos no dicionário
dicionario['sexo'] = 'Feminino'
print(dicionario)

# Exemplo 5
# Removendo elementos do dicionário
del dicionario['cidade']
print(dicionario)

# Exemplo 6
# Funções built-in
# len() - Retorna o número de elementos do dicionário
print(len(dicionario))

# Exemplo 7
# Funções built-in
# clear() - Remove todos os elementos do dicionário
dicionario.clear()
print(dicionario)