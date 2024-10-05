# Exercício 9 do Capítulo 2 das Listas de Linguagem de Programação - ECT3201

def main():
    conjunto_a = set() # Conjunto Vazio
    conjunto_b = set() # Conjunto Vazio

    numero1 = int(input(""))  # Ler o valor de um número inteiro distindo
    conjunto_a.add(numero1) # .add aqui é para o programa tenha valores únicos

    numero2 = int(input(""))
    conjunto_a.add(numero2)

    numero3 = int(input(""))
    conjunto_a.add(numero3)

    numero4 = int(input(""))
    conjunto_b.add(numero4)

    numero5 = int(input(""))
    conjunto_b.add(numero5)

    numero6 = int(input(""))
    conjunto_b.add(numero6)

    print("União:", conjunto_a | conjunto_b) # Realiza a União entre os conjuntos a e b
    print("Interseção:", conjunto_a & conjunto_b) # Realiza Interseção entre os conjuntos a e b
    print("Diferença:", conjunto_a - conjunto_b) # Realiza Diferença entre os conjuntos a e b

if __name__ == "__main__":
    main()
