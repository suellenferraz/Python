# Exercício 2 do Capítulo 2 das Listas de Linguagem de Programação - ECT3201
"""Escreva um programa que solicite ao usuário que insira uma palavra ou frase. Em seguida, o programa deve imprimir o comprimento da string, a primeira letra da string, a última letra da string e a string invertida."""

def main():
    texto = input("") 
    tamanho = len(texto) # len é usado para calcular o tamanho de uma string
    print(tamanho) # Comprimento da string
    print(texto[0]) # Primeira letra da string
    print(texto[-1]) # Última letra da string
    print(texto[::-1]) # String invertida
    
if __name__ == "__main__":
    main()   