# Exercício 5 do Capítulo 2 das Listas de Linguagem de Programação - ECT3201
"""Crie um programa que solicite ao usuário que insira cinco diferentes frutas. Em seguida, crie uma lista chamada “frutas” com as frutas fornecidas pelo usuário e imprima a lista completa na tela."""

def main():
    fruta1 = input("") # Foi criado 5 leituras de valor para a lista.
    fruta2 = input("")
    fruta3 = input("")
    fruta4 = input("")
    fruta5 = input("")

    frutas = [fruta1, fruta2, fruta3, fruta4, fruta5] # Criação da lista com as variáveis.
    print(f"Lista de frutas: {frutas}")
    
if __name__ == "__main__":
    main()