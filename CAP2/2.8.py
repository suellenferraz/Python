# Exercício 8 do Capítulo 2 das Listas de Linguagem de Programação - ECT3201

def main():
    
    numeros = set() # Conjunto Vazio
    
    Valor1 = int(input("")) # Ler o valor de um número inteiro distindo
    numeros.add(Valor1) # .add aqui é para o programa tenha valores únicos
    
    Valor2 = int(input(""))
    numeros.add(Valor2)
    
    Valor3 = int(input(""))
    numeros.add(Valor3)
    
    Valor4 = int(input(""))
    numeros.add(Valor4)
    
    Valor5 = int(input(""))
    numeros.add(Valor5)

    print(numeros)
    
if __name__ == "__main__":
    main()
