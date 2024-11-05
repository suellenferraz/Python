# Exercício 1 do Capítulo 3 das Listas de Linguagem de Programação - ECT3201
"""Dada a expressão matemática: a=4*(2+3)-7.
Crie uma variável chamada a e atribua a ela o resultado dessa expressão. Em seguida, crie uma variável chamada b e atribua a ela o valor de a multiplicado por 2. Por fim, imprima os valores de a e b."""

def main ():
    a = 4*(2+3)-7 # Expressão matemática 
    b = a*2 # Resultado multiplicado por 2
    
    print(f"O valor de 'a' é: {a}")
    print(f"O valor de 'b' é: {b}")
    
if __name__ == "__main__":
    main()