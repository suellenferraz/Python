# Manipulação de strings, Concatenação, interpolação, formatação, etc.

# Concatenação é a junção de duas ou mais strings em uma única string
nome = 'João' # String
sobrenome = 'Silva' # String
nome_completo = nome + ' ' + sobrenome # Concatenação de strings com operador de adição (+) 
print(nome_completo) # Saída: João Silva

# Interpolação é a substituição de variáveis dentro de uma string por seus respectivos valores 
nome_completo = '%s %s' % (nome, sobrenome) # Interpolação de strings com operador de módulo (%)
print(nome_completo) # Saída: João Silva

# Formatação é a substituição de variáveis dentro de uma string por seus respectivos valores
nome_completo = '{} {}'.format(nome, sobrenome) # Formatação de strings com método format()
print(nome_completo) # Saída: João Silva

# F-strings é a substituição de variáveis dentro de uma string por seus respectivos valores
nome_completo = f'{nome} {sobrenome}' # F-strings
print(nome_completo) 

# Funções de manipulação de strings 
nome = 'joão silva' # String
print(nome.capitalize()) # Saída: João silva, capitaliza a primeira letra da string
print(nome.title()) # Saída: João Silva, capitaliza a primeira letra de cada palavra da string
print(nome.upper()) # Saída: JOÃO SILVA, converte todas as letras da string para maiúsculas
print(nome.lower()) # Saída: joão silva, converte todas as letras da string para minúsculas
print(nome.swapcase()) # Saída: JOÃO SILVA, converte letras maiúsculas em minúsculas e vice-versa
print(nome.replace('joão', 'maria')) # Saída: maria silva, substitui uma substring por outra
print(nome.count('a')) # Saída: 1, conta o número de ocorrências de uma substring
print(nome.find('a')) # Saída: 3, retorna o índice da primeira ocorrência de uma substring
print(nome.startswith('joão')) # Saída: True, verifica se a string começa com uma substring
print(nome.endswith('silva')) # Saída: True, verifica se a string termina com uma substring
print(nome.split(' ')) # Saída: ['joão', 'silva'], divide a string em uma lista de substrings
print(nome.strip()) # Saída: joão silva, remove espaços em branco do início e do fim da string
print(nome.rstrip()) # Saída: joão silva, remove espaços em branco do fim da string
print(nome.lstrip()) # Saída: joão silva, remove espaços em branco do início da string