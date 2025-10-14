# Exercício 2 do Capítulo 4 das Listas de Linguagem de Programação - ECT3201

# Verificação de Palíndromo: Faça um programa que receba uma lista de palavras e verifique se cada palavra é um palíndromo. Um palíndromo é uma palavra que permanece a mesma quando lida de trás para frente. O programa deve imprimir “Sim” para palíndromos e “Não” para não palíndromos. Utilize end=' ' no comando print para que os resultados sejam exibidos na mesma linha, separados por espaços.
# Exemplo de entrada: arara python reviver código osso copilot radar programa mussum piloto

def main():
    palavras = input().split() # Recebe uma lista de palavras separadas por espaço 
    for palavra in palavras: # Loop que verifica se cada palavra é um palíndromo 
        if palavra == palavra[::-1]: # Verifica se a palavra é igual à palavra lida de trás para frente 
            print("Sim", end=' ') # Imprime "Sim" se a palavra for um palíndromo 
        else: # Caso contrário
            print("Não", end=' ') # Imprime "Não" se a palavra não for um palíndromo
if __name__ == "__main__":
    main()