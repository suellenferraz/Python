# Exercício 10 do Capítulo 2 das Listas de Linguagem de Programação - ECT3201
"""Dada duas strings fornecidas pelo usuário, realize as seguintes operações e imprima os resultados:
Transformar em maiúsculas: Converta toda a primeira string para letras maiúsculas.
Transformar em minúsculas: Converta toda a segunda string para letras minúsculas.
Concatenar as strings: Combine a primeira e a segunda string em uma única string.
Imprimir o resultado: Exiba a string concatenada na tela."""

def main():
    x = input() # Ler os valores de entrada
    y = input()
    
    maiusculas = x.upper() # Transforma uma string toda em maiúscula
    minusculas = y.lower() # Transforma uma string toda em minúscula
    concatenar = f"{x.upper()} {y.lower()}" # Junta as duas strings em uma só
    
    print(maiusculas)
    print(minusculas)
    print(concatenar)
    
if __name__ == "__main__":
    main()