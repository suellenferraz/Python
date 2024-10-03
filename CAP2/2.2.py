# Exercício 2 do Capítulo 2 das Listas de Linguagem de Programação - ECT3201

def main():
    texto = input("") 
    tamanho = len(texto) # len é usado para calcular o tamanho de uma string
    print(tamanho) # Comprimento da string
    print(texto[0]) # Primeira letra da string
    print(texto[-1]) # Última letra da string
    print(texto[::-1]) # String invertida
    
if __name__ == "__main__":
    main()   