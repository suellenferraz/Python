# Exercício 5 do Capítulo 4 das Listas de Linguagem de Programação - ECT3201

# Cálculo do Fatorial: Escreva um programa que receba uma lista de números inteiros, e obedecendo alguns critérios, calcule e imprima o fatorial de cada um deles. O fatorial de um número é o produto de todos os números inteiros de 1 até o próprio número.
""" Aqui estão as etapas e critérios para implementar seu programa:

Receba e armazene uma lista de números inteiros.
Verifique se cada número é válido (ou seja, maior ou igual a zero e menor do que 15).
Calcule o fatorial de cada número usando um loop for ou while.
Exiba o resultado do fatorial para cada um dos números. Se não for possível calcular o fatorial (por exemplo, para números não válidos), escreva um X.
Mostre a quantidade de números para os quais não foi possível calcular o fatorial."""

def main():
    numeros = map(int, input().replace(',', '').split()) # Recebe uma lista de números inteiros e converte para uma lista de inteiros separados por vírgula e espaço
    invalidos = 0 # Inicializa o contador de números inválidos
    resultados = [] # Inicializa uma lista vazia para armazenar os resultados dos fatoriais

    for numero in numeros: # Loop que calcula o fatorial de cada número na lista
        if numero < 0 or numero >= 15: # Verifica se o número é inválido
            resultados.append('X') # Adiciona 'X' à lista de resultados
            invalidos += 1 # Incrementa o contador de números inválidos
        else: # Caso contrário
            fatorial = 1 # Inicializa a variável fatorial como 1
            for i in range(1, numero + 1): # Loop que calcula o fatorial do número
                fatorial *= i # Calcula o fatorial do número multiplicando o valor atual de fatorial por i
            resultados.append(str(fatorial)) # Adiciona o fatorial do número à lista de resultados como string 

    print(" ".join(resultados)) # Imprime os resultados dos fatoriais separados por espaço 
    print(f'Quantidade de números inválidos: {invalidos}') # Imprime a quantidade de números inválidos

if __name__ == '__main__':
    main()
