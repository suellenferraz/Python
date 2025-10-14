# Exercício 3 do Capítulo 3 das Listas de Linguagem de Programação - ECT3201
"""Escreva um programa que converta uma temperatura de Celsius para Fahrenheit. Utilize a fórmula: F = (9/5)*C+32, onde F é a temperatura em Fahrenheit e C é a temperatura em Celsius.
Solicite ao usuário que digite a temperatura em Celsius.
Em seguida, converta a temperatura digitada para Fahrenheit utilizando a fórmula fornecida.
Por fim, exiba na tela o resultado da conversão para o usuário, formatado com 2 casas decimais.
"""

def main():
    C = float(input("")) # Entrada em ponto flutuante (float) do Celsius
    fahrenheit = (9/5)*C+32 # Fórmula de conversão de Celsius para Fahrenheit
    
    print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}") # Saída com 2 casas decimais (:.2f)

if __name__ == "__main__":
    main()