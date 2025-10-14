# Exercício 6 do Capítulo 2 das Listas de Linguagem de Programação - ECT3201
"""Escreva um programa em solicite ao usuário que insira duas coordenadas (x e y). Em seguida, crie uma tupla chamada coordenadas com essas coordenadas e imprima o conteúdo da tupla na tela."""

def main():
    x = float(input("")) # Ler o valor da coordenada x
    y = float(input("")) # Ler o valor da coordenada y
    coordenada = (x,y) # Tupla da coordenada de x,y
    
    print(f"Coordenadas: {coordenada}")

if __name__ == "__main__":
    main()