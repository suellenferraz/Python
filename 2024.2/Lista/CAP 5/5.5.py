# Exercício 5 do Capítulo 5 das Listas de Linguagem de Programação - ECT3201

import math # Importa a biblioteca math.

def ler_dados(): # Função que lê os dados de entrada
    a, b, c = map(float, input().split(",")) # Lê os valores de a, b e c separados por vírgula e converte para float.
    return a, b, c # Retorna os valores de a, b e c.

def verificar_raizes(a,b,c): # Função que verifica se é possível calcular as raízes.
    if a == 0: # Se a for igual a 0.
        return False # Retorna falso.
    elif b**2 - 4*a*c < 0: # Se b² - 4ac for menor que 0.
        return False # Retorna falso.
    else:  # Se não.
        return True # Retorna verdadeiro.

def calcular_raizes(a,b,c): # Função que calcula as raízes.
    delta = b**2 - 4*a*c # Calcula o delta.
    x1 = (-b + math.sqrt(delta))/(2*a) # Calcula a primeira raiz.
    x2 = (-b - math.sqrt(delta))/(2*a) # Calcula a segunda raiz.
    return x1, x2 

a, b, c = ler_dados() # Chama a função ler_dados e atribui os valores de a, b e c.
if verificar_raizes(a,b,c): # Se for possível calcular as raízes.
    x1, x2 = calcular_raizes(a,b,c) # Chama a função calcular_raizes e atribui os valores de x1 e x2.
    print(f'R1 = {x1:.2f}') # Imprime o valor de x1 com 2 casas decimais.
    print(f'R2 = {x2:.2f}') # Imprime o valor de x2 com 2 casas decimais.
else: # Se não.
    print("Impossível calcular") # Imprime "Impossível calcular".