# Operadores de associação é um tipo de operador que permite verificar se um valor está presente em uma sequência de valores. Os operadores de associação são in e not in. Eles são usados para verificar se um valor está presente em uma sequência de valores, como uma lista, tupla, dicionário ou string.

# Exemplo:
# Verifica se o valor 5 está presente na lista [1, 2, 3, 4, 5].
print(5 in [1, 2, 3, 4, 5])  # True
# Verifica se o valor 6 está presente na lista [1, 2, 3, 4, 5].
print(6 in [1, 2, 3, 4, 5])  # False

# Verifica se o valor 'a' está presente na string 'Python'.
print('a' in 'Python')  # False
# Verifica se o valor 'z' está presente na string 'Python'.
print('z' in 'Python')  # False

# Verifica se a chave 'nome' está presente no dicionário {'nome': 'João', 'idade': 30}.
print('nome' in {'nome': 'João', 'idade': 30})  # True
# Verifica se a chave 'email' está presente no dicionário {'nome': 'João', 'idade': 30}.
print('email' in {'nome': 'João', 'idade': 30})  # False

# Verifica se o valor 5 não está presente na lista [1, 2, 3, 4, 5].
print(5 not in [1, 2, 3, 4, 5])  # False
# Verifica se o valor 6 não está presente na lista [1, 2, 3, 4, 5].
print(6 not in [1, 2, 3, 4, 5])  # True

# Verifica se o valor 'a' não está presente na string 'Python'.
print('a' not in 'Python')  # True
# Verifica se o valor 'z' não está presente na string 'Python'.
print('z' not in 'Python')  # True
