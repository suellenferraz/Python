# Exercício 7 do Capítulo 4 das Listas de Linguagem de Programação - ECT3201

# Exercício de Padrão de Asteriscos: Escreva um programa em Python que imprima um triângulo de asteriscos. O programa deve receber na entrada o número de linhas do triângulo e o tipo de triângulo a ser impresso (tipo1 ou tipo2). Em seguida, o programa deve imprimir o triângulo de asteriscos com o número de linhas especificado e no formato escolhido.
""" Tipo 1: Cada linha começa com um asterisco e aumenta o número de asteriscos à medida que descemos.
Tipo 2: O número máximo de asteriscos aparece na primeira linha e à medida que avançamos para a direita, este número vai diminuindo."""

def main():
    tipo, n = input().split(", ") # Recebe o tipo de triângulo e o número de linhas do triângulo
    n = int(n) # Converte o número de linhas do triângulo de string para inteiro
    if tipo == "tipo1": # Verifica se o tipo de triângulo é tipo1
        for i in range(1, n+1): # Loop que imprime o triângulo de asteriscos
            print("*"*i) # Imprime a linha do triângulo de asteriscos
    elif tipo == "tipo2": # Verifica se o tipo de triângulo é tipo2
        for i in range(n, 0, -1): # Loop que imprime o triângulo de asteriscos
            print("*"*i) # Imprime a linha do triângulo de asteriscos
if __name__ == "__main__":
    main()