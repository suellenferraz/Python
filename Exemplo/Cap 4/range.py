# Exemplos básicos de como utiliza a função range e laços de repetição (for) em Python e operador in.

# Exemplo base

def main():
    for i in range(5): # for é um laço de repetição que percorre uma sequência de valores, que nesse caso é de 0 a 4
        print(i) 
if __name__ == "__main__":
    main()
    
# Listas

def main():
    frutas = ["maçã", "banana", "laranja"] # lista de frutas
    for fruta in frutas: # para cada fruta na lista de frutas
        print(f"Fruta: {fruta}") # imprime a fruta
if __name__ == "__main__":
    main()

# Strings

def main():
    palavra = "Python" # string
    for letra in palavra: # para cada letra na string
        print(letra) # imprime a letra
if __name__ == "__main__":
    main()
    
# Executando um número específico de vezes

def main():
    for _ in range(5):
        print("Executando 5 vezes")
if __name__ == "__main__":
    main()
    
# Loop aninhado com matriz

def main(): # matriz é uma lista de listas
    matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
    # percorre a matriz
    for linha in matriz:
        for elemento in linha: # para cada elemento na linha
            print(elemento)

if __name__ == "__main__":
    main()

# Loop com 2 grupos de elementos 

def main():
    cores = ["vermelho", "azul", "verde"] # lista de cores
    tamanhos = ["P", "M", "G"] # lista de tamanhos

    for cor in cores: # para cada cor na lista de cores
        for tamanho in tamanhos: # para cada tamanho na lista de tamanhos
            print(f"{cor} - {tamanho}") # imprime a cor e o tamanho
if __name__ == "__main__":
    main()