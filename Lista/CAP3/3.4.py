# Exercício 4 do Capítulo 3 das Listas de Linguagem de Programação - ECT3201
"""Escreva um programa que recebe na entrada um número inteiro entre 10 e 20. O programa deverá converter esse número para sua representação binária, removendo o prefixo '0b' da conversão. Em seguida, cada bit dessa representação binária será salvo em uma lista, onde cada posição da lista conterá um dos bits. Por fim, o programa deverá imprimir o resultado."""

def main():
    numero = int(input("")) # Entrada de um número inteiro

    if numero < 10 or numero > 20: # Número inteiro entre 10 e 20
        print("O número inserido não está dentro do intervalo permitido.")
        
    else:
        numero_binario = bin(numero)[2:] # Converte para binário e remove ([2:]) o prefixo '0b' 
        lista = list(numero_binario) # Converte a string binária para uma lista de caracteres
        print(lista)

if __name__ == "__main__":
    main()