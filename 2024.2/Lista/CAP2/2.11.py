# Exercício 11 do Capítulo 2 das Listas de Linguagem de Programação - ECT3201
"""Você deve criar um programa que verifica se os números em uma lista são pares ou ímpares. A lista possui tamanho 5 e será fornecida pelo usuário. Cada número na lista deve ser avaliado individualmente, sem o uso de estruturas de repetição (como loops). O programa deve exibir na tela se cada número é par ou ímpar."""

def main():
    # Ler os valores de uma lista de tamanho 5, conforme enunciado
    numero1 = int(input(""))
    numero2 = int(input(""))
    numero3 = int(input(""))
    numero4 = int(input(""))
    numero5 = int(input("")) 
    # Preferi utilizar um por um, usando if e else, devido que não podia usar loop.
    if numero1 % 2 == 0: # Verifica se o número é par ou ímp, se o resto da divisão por 2 for 0, é par.
        print(f"O número {numero1} é par.")
    else:
        print(f"O número {numero1} é ímpar.")
    
    if numero2 % 2 == 0:
        print(f"O número {numero2} é par.")
    else:
        print(f"O número {numero2} é ímpar.")
    
    if numero3 % 2 == 0:
        print(f"O número {numero3} é par.")
    else:
        print(f"O número {numero3} é ímpar.")
    
    if numero4 % 2 == 0:
        print(f"O número {numero4} é par.")
    else:
        print(f"O número {numero4} é ímpar.")
    
    if numero5 % 2 == 0:
        print(f"O número {numero5} é par.")
    else:
        print(f"O número {numero5} é ímpar.")
    
if __name__ == "__main__":
    main()