# Exercício 11 do Capítulo 2 das Listas de Linguagem de Programação - ECT3201

def main():
    # Ler os valores de uma lista de tamanho 5, conforme enunciado
    numero1 = int(input(""))
    numero2 = int(input(""))
    numero3 = int(input(""))
    numero4 = int(input(""))
    numero5 = int(input("")) 
    # Preferi utilizar um por um, usando if e else, devido que não podia usar loop.
    if numero1 % 2 == 0:
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