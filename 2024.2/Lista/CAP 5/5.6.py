# Exercício 6 do Capítulo 5 das Listas de Linguagem de Programação - ECT3201

def contar_pares_impares(lista): # Função que conta a quantidade de números pares e ímpares.
    pares = 0 # Variável que armazena a quantidade de números pares.
    impares = 0 # Variável que armazena a quantidade de números ímpares.
    for i in lista: # Para cada número na lista.
        if i % 2 == 0: # Se o número for par. Usa o operador módulo para verificar se o número é par. Se o resto da divisão por 2 for 0, o número é par.
            pares += 1 # Adiciona 1 à quantidade de números pares.
        else: # Se não.
            impares += 1 # Adiciona 1 à quantidade de números ímpares.
    return pares, impares # Retorna a quantidade de números pares e ímpares.

def contar_positivos_negativos(lista): # Função que conta a quantidade de números positivos e negativos.
    positivos = 0 # Variável que armazena a quantidade de números positivos.
    negativos = 0 # Variável que armazena a quantidade de números negativos.
    for i in lista: # Para cada número na lista.
        if i > 0: # Se o número for positivo.
            positivos += 1 # Adiciona 1 à quantidade de números positivos.
        else: # Se não.
            negativos += 1 # Adiciona 1 à quantidade de números negativos.
    return positivos, negativos # Retorna a quantidade de números positivos e negativos.

lista = list(map(int, input().split())) # Lê a lista de números separados por espaço e converte para inteiros.
pares, impares = contar_pares_impares(lista) # Chama a função contar_pares_impares e atribui os valores de pares e ímpares.
positivos, negativos = contar_positivos_negativos(lista) # Chama a função contar_positivos_negativos e atribui os valores de positivos e negativos.
print(f'Quantidade de números pares: {pares}') # Imprime a quantidade de números pares.
print(f'Quantidade de números ímpares: {impares}') # Imprime a quantidade de números ímpares.
print(f'Quantidade de números positivos: {positivos}') # Imprime a quantidade de números positivos.
print(f'Quantidade de números negativos: {negativos}') # Imprime a quantidade de números negativos.