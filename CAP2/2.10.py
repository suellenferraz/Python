# Exercício 10 do Capítulo 2 das Listas de Linguagem de Programação - ECT3201

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