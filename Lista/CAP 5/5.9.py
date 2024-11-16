# Exercício 9 do Capítulo 5 das Listas de Linguagem de Programação - ECT3201

def calcular_potencia(base, expoente): # Função que calcula a potência de um número de forma recursiva.
    if expoente == 0: # Se o expoente for igual a 0.
        return 1 # Retorna 1.
    return base * calcular_potencia(base, expoente - 1) # Retorna a base multiplicada pela chamada recursiva da função com o expoente decrementado em 1.

base, expoente = map(int, input().split(',')) # Lê a base e o expoente separados por vírgula e converte para inteiros.
print(f'{base}^{expoente} = {calcular_potencia(base, expoente)}') # Imprime a base elevada ao expoente.