# Lista é uma coleção ordenada de itens.
# Em Python, listas são representadas por colchetes [] e os elementos são separados por vírgulas.

# Exemplo de listas
a = [1, 2, 3, 4, 5]

# Imprimindo a lista
print(a) # [1, 2, 3, 4, 5]

# Adicionando elementos em uma lista
a.append(6)

# Imprimindo a lista
print(a) # [1, 2, 3, 4, 5, 6]

# Removendo elementos de uma lista
a.remove(6)

# Imprimindo a lista
print(a) # [1, 2, 3, 4, 5]

# Acessando elementos de uma lista
print(a[0]) # 1
print(a[1]) # 2
print(a[2]) # 3
print(a[3]) # 4
print(a[4]) # 5

# Acessando elementos de uma lista de forma reversa
print(a[-1]) # 5
print(a[-2]) # 4
print(a[-3]) # 3
print(a[-4]) # 2
print(a[-5]) # 1

# Acessando um intervalo de elementos de uma lista
print(a[0:2]) # [1, 2]
print(a[1:3]) # [2, 3]
print(a[2:4]) # [3, 4]
print(a[3:5]) # [4, 5]

# Acessando um intervalo de elementos de uma lista de forma reversa
print(a[-5:-3]) # [1, 2]
print(a[-4:-2]) # [2, 3]
print(a[-3:-1]) # [3, 4]
print(a[-2:]) # [4, 5]

# Verificando se um elemento está presente em uma lista
print(1 in a) # True
print(2 in a) # True
print(3 in a) # True
print(4 in a) # True
print(5 in a) # True
print(6 in a) # False

# Verificando o tamanho de uma lista
print(len(a)) # 5

# Concatenando listas
b = [6, 7, 8, 9, 10]
c = a + b

# Imprimindo a lista
print(c) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Repetindo elementos de uma lista
d = a * 2

# Imprimindo a lista
print(d) # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# Ordenando uma lista
e = [5, 3, 1, 4, 2]
e.sort()

# Imprimindo a lista
print(e) # [1, 2, 3, 4, 5]

# Invertendo uma lista
e.reverse()

# Imprimindo a lista
print(e) # [5, 4, 3, 2, 1]

# Limpando uma lista
e.clear()

# Imprimindo a lista
print(e) # []

# Adicionando elementos em uma lista
e.append(1)

# Imprimindo a lista
print(e) # [1]

# Adicionando elementos em uma lista
e.append(2)

# Imprimindo a lista
print(e) # [1, 2]

# Adicionando elementos em uma lista
e.append(3)
e.append(4)
e.append(5)

# Imprimindo a lista
print(e) # [1, 2, 3, 4, 5]

# Removendo elementos de uma lista
e.pop()

# Imprimindo a lista
print(e) # [1, 2, 3, 4]

# Removendo elementos de uma lista
e.pop()

# Imprimindo a lista
print(e) # [1, 2, 3]

# Removendo elementos de uma lista
e.pop()

# Imprimindo a lista
print(e) # [1, 2]

# Removendo elementos de uma lista
e.pop()

# Imprimindo a lista
print(e) # [1]

# Removendo elementos de uma lista
e.pop()

# Imprimindo a lista
print(e) # []

# Adicionando elementos em uma lista
e.append(1)
e.append(2)
e.append(3)
e.append(4)
e.append(5)

# Imprimindo a lista
print(e) # [1, 2, 3, 4, 5]

# Removendo elementos de uma lista
e.remove(5)
e.remove(4)
e.remove(3)
e.remove(2)
e.remove(1)

# Imprimindo a lista
print(e) # []
