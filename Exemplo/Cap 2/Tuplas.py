# Tuplas é uma coleção de elementos ordenada e imutável.
# Tuplas são definidas por parênteses e vírgulas.
# Tuplas são imutáveis, ou seja, não é possível alterar seus elementos.
# Tuplas são indexadas, ou seja, cada elemento possui um índice.
# Tuplas podem conter elementos de diferentes tipos.
# Tuplas podem conter outras tuplas.
# Tuplas podem ser usadas como chaves de dicionários.
# Tuplas são mais rápidas que listas.

# Criando uma tupla vazia
tupla = ()
print(tupla)

# Criando uma tupla com um elemento
tupla = (1,)
print(tupla)

# Criando uma tupla com vários elementos
tupla = (1, 2, 3)
print(tupla)

# Criando uma tupla com elementos de diferentes tipos
tupla = (1, 'a', 2.5)
print(tupla)

# Criando uma tupla com outras tuplas
tupla = (1, (2, 3), (4, 5))
print(tupla)

# Criando uma tupla com a função tuple()
tupla = tuple([1, 2, 3])
print(tupla)

# Criando uma tupla com a função tuple()
tupla = tuple('abc')
print(tupla)

# Acessando elementos de uma tupla
tupla = (1, 2, 3)
print(tupla[0])
print(tupla[1])
print(tupla[2])

# Acessando elementos de uma tupla
tupla = (1, 2, 3)
print(tupla[-1])
print(tupla[-2])
print(tupla[-3])

# Acessando elementos de uma tupla
tupla = (1, 2, 3)
print(tupla[0:2])
print(tupla[:2])
print(tupla[1:3])
print(tupla[1:])
print(tupla[:])

# Acessando elementos de uma tupla
tupla = (1, 2, 3)
print(tupla.index(1))

# Acessando elementos de uma tupla
tupla = (1, 2, 3)
print(tupla.count(1))

# Concatenando tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla = tupla1 + tupla2
print(tupla)

# Repetindo elementos de uma tupla
tupla = (1, 2, 3)
tupla = tupla * 3
print(tupla)

# Verificando se um elemento pertence a uma tupla
tupla = (1, 2, 3)
print(1 in tupla)
print(4 in tupla)

# Verificando o tamanho de uma tupla
tupla = (1, 2, 3)
print(len(tupla))

# Iterando sobre uma tupla
tupla = (1, 2, 3)
for elemento in tupla:
    print(elemento)

# Iterando sobre uma tupla
tupla = (1, 2, 3)
for indice, elemento in enumerate(tupla):
    print(indice, elemento)
    
# Desempacotando uma tupla
tupla = (1, 2, 3)
a, b, c = tupla
print(a)
print(b)
print(c)

# Desempacotando uma tupla
tupla = (1, 2, 3)
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

# Desempacotando uma tupla
tupla = (1, 2, 3)
a, b, c = [1, 2, 3]
print(a)
print(b)
print(c)

# Desempacotando uma tupla
tupla = (1, 2, 3)
a, b, c = '123'
print(a)
print(b)
print(c)

# Desempacotando uma tupla
tupla = (1, 2, 3)
a, b, c = 'abc'
print(a)
print(b)
print(c)

# Desempacotando uma tupla
tupla = (1, 2, 3)
a, b, c = 'a', 'b', 'c'
print(a)
print(b)
print(c)