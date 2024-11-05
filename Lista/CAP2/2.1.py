# Exercício 1 do Capítulo 2 das Listas de Linguagem de Programação - ECT3201

""" Escreva um programa que solicita ao usuário dois valores, um do tipo inteiro (int) e outro do tipo ponto flutuante (float). Após receber esses valores como entrada, o programa deve atribuí-los a duas variáveis distintas e, em seguida, imprimir na tela o resultado das seguintes operações matemáticas:
Soma dos dois valores.
Subtração do valor do tipo float pelo valor do tipo inteiro.
Multiplicação dos dois valores.
Divisão do valor do tipo inteiro pelo valor do tipo float.
Certifique-se de formatar adequadamente a saída dos resultados."""

def main():
    x = int(input("")) # Ler um valor inteiro
    y = float(input("")) # Ler um de ponto flutuante
    soma = x+y
    subtracao = x-y
    multiplicacao = x*y
    divisao = x/y
    print(f"Soma: {soma}\nSubtração: {subtracao}\nMultiplicação: {multiplicacao}\nDivisão: {divisao}")
    # Usei o fstrings para incoporar as variáveis dentro da strings, assim fica mais legível.

if __name__ == "__main__":
    main()