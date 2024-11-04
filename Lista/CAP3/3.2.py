# Exercício 2 do Capítulo 3 das Listas de Linguagem de Programação - ECT3201

def main():
    usuario = int(input("")) # Entrada do valor inteiro
    
    if usuario < 100 or usuario > 1000: # Como tem que um número interio positivo entre 100 e 1000, utilizamos o usuario <100 e >1000.
        print("Por favor, insira um número inteiro positivo entre 100 e 1000.")
    else:
        resto = usuario % 5 # Resto da divisão do número inteiro positivo por 5.
        print(f"O resto da divisão de {usuario} por 5 é {resto}.")

if __name__ == "__main__":
    main()