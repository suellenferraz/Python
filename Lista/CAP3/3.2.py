# Exercício 2 do Capítulo 3 das Listas de Linguagem de Programação - ECT3201
"""Escreva um programa que solicita ao usuário um número inteiro positivo entre 100 e 1000. Em seguida, o programa deve calcular o resto da divisão desse número por 5, armazenar o resultado em uma variável chamada resto e imprimir este valor.
Certifique-se de que o programa lide adequadamente com entradas inválidas. Caso o usuário insira um número negativo ou fora do intervalo especificado, exiba a seguinte mensagem de erro: “Por favor, insira um número inteiro positivo entre 100 e 1000.”"""

def main():
    usuario = int(input("")) # Entrada do valor inteiro
    
    if usuario < 100 or usuario > 1000: # Como tem que um número interio positivo entre 100 e 1000, utilizamos o usuario <100 e >1000.
        print("Por favor, insira um número inteiro positivo entre 100 e 1000.")
    else:
        resto = usuario % 5 # Resto da divisão do número inteiro positivo por 5.
        print(f"O resto da divisão de {usuario} por 5 é {resto}.")

if __name__ == "__main__":
    main()