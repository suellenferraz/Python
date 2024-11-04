# Exercício 1 do Capítulo 2 das Listas de Linguagem de Programação - ECT3201

def main():
    x = int(input("")) # Ler um valor inteiro
    y = float(input("")) # Ler um de ponto flutuante
    soma = x+y
    subtracao = x-y
    multiplicacao = x*y
    divisao = x/y
    print(f"Soma: {soma}\nSubtração: {subtracao}\nMultiplicação: {multiplicacao}\nDivisão: {divisao}")
    # Usei o fstrings para incoporar as variáveis dentro da strings, assim fica mais legível.

if __name__ == "__main__":
    main()