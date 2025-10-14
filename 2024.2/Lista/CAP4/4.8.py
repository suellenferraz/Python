# Exercício 8 do Capítulo 4 das Listas de Linguagem de Programação - ECT3201

# Identificação de Números Primos em uma Lista: Desenvolva um programa que identifique todos os números primos presentes em uma lista fornecida na entrada. Um número primo é um número maior que 1 que não possui divisores positivos além de 1 e si próprio. Siga as Instruções a seguir:
""" Leia uma lista de números inteiros.
Para cada número na lista, verifique se ele é um número primo.
Se o número for primo, adicione-o a uma nova lista.
Após verificar todos os números na lista original, exiba a nova lista contendo apenas os números primos."""

def main():
    entrada = input("") # Recebe uma lista de números inteiros
    lista = entrada.replace(',', ' ').split() # Converte a lista de números inteiros em uma lista de strings
    primos = [] # Inicializa uma lista vazia para armazenar os números primos

    for num in lista: # Loop que verifica se cada número na lista é um número primo
        i = int(num) # Converte o número de string para inteiro
        if i > 1: # Verifica se o número é maior que 1
            is_primo = True # Inicializa a variável is_primo como True
            for j in range(2, int(i**0.5) + 1): # Loop que verifica se o número é primo
                if i % j == 0: # Verifica se o número é divisível por j
                    is_primo = False # Atualiza a variável is_primo para False
                    break # Encerra o loop
            if is_primo: # Verifica se o número é primo
                primos.append(i) # Adiciona o número à lista de números primos

    print(', '.join(map(str, primos))) # Exibe a nova lista contendo apenas os números primos separados por vírgula e espaço

if __name__ == '__main__':
    main()