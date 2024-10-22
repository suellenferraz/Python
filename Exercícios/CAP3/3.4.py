# Exercício 4 do Capítulo 3 das Listas de Linguagem de Programação - ECT3201

def main():
    numero = int(input("")) # Entrada de um número inteiro

    if numero < 10 or numero > 20: # Número inteiro entre 10 e 20
        print("O número inserido não está dentro do intervalo permitido.")
        
    else:
        numero_binario = bin(numero)[2:] # Converte para binário e remove ([2:]) o prefixo '0b' 
        lista = list(numero_binario) # Converte a string binária para uma lista de caracteres
        print(lista)

if __name__ == "__main__":
    main()