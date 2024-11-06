# Conjuntos são coleções de elementos únicos, ou seja, não há repetição de elementos. 
# Em Python, conjuntos são representados por chaves {} e elementos separados por vírgulas.

# Exemplo de conjuntos
a = {1, 2, 3, 4, 5}
print(a) # {1, 2, 3, 4, 5}

# Conjuntos não possuem índices
# print(a[0]) # Erro

# Adicionando elementos em um conjunto
a.add(6)
print(a) # {1, 2, 3, 4, 5, 6}

# Removendo elementos de um conjunto
a.remove(6)
print(a) # {1, 2, 3, 4, 5}

# Verificando se um elemento está presente em um conjunto
print(1 in a) # True
print(6 in a) # False

# União de conjuntos
b = {4, 5, 6, 7, 8}
print(a.union(b)) # {1, 2, 3, 4, 5, 6, 7, 8}

# Interseção de conjuntos
print(a.intersection(b)) # {4, 5}

# Diferença de conjuntos
print(a.difference(b)) # {1, 2, 3}

# Diferença simétrica de conjuntos
print(a.symmetric_difference(b)) # {1, 2, 3, 6, 7, 8}

# Conjunto vazio
c = set()
print(c) # set()

# Conjunto com elementos
d = set([1, 2, 3, 4, 5])
print(d) # {1, 2, 3, 4, 5}

# Conjunto com elementos repetidos
e = set([1, 2, 2, 3, 3, 4, 4, 5, 5])
print(e) # {1, 2, 3, 4, 5}

# Conjunto com elementos de diferentes tipos
f = set([1, 2, 3, 'a', 'b', 'c'])
print(f) # {1, 2, 3, 'a', 'b', 'c}
