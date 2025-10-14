# Exercício 10 do Capítulo 4 das Listas de Linguagem de Programação - ECT3201

# O “Velho” Fibonacci: A sequência de Fibonacci é uma série infinita de números inteiros em que cada número é a soma dos dois anteriores. Ela começa com os números 1 e 1:
""" 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, …
Para calcular o próximo número na sequência, somamos os dois números anteriores. Por exemplo:
O terceiro número é 1 + 1 = 2.
O quarto número é 1 + 2 = 3.
O quinto número é 2 + 3 = 5.
E assim por diante. 
Agora, vamos criar um programa que gere a sequência de Fibonacci até o n-ésimo termo. O usuário fornecerá o valor de n.
Inicializamos as variáveis ultimo e penultimo com os valores 1, pois os dois primeiros termos da sequência são 1.
Usamos um laço de repetição (como um for ou while) para calcular os próximos termos. Salvando os valores em uma lista.
A cada iteração, somamos ultimo e penultimo para obter o próximo termo.
Atualizamos as variáveis ultimo e penultimo para os valores corretos.
Repetimos o processo até chegarmos ao n-ésimo termo.
Por fim, todos os números da sequência, armazenados em uma lista, devem ser impressos."""

def main():
    n = int(input("")) # Número de termos da sequência de Fibonacci
    fib = [1, 1] # Inicializando a lista com os dois primeiros termos da sequência

    for i in range(2, n): # Calculando os próximos termos da sequência
        fib.append(fib[i - 1] + fib[i - 2]) # Adicionando o próximo termo à lista

    for i in range(n): # Imprimindo os termos da sequência
        if i < n - 1: # Se não for o último termo, imprime com vírgula
            print(fib[i], end=", ") 
        else: # Se for o último termo, imprime sem vírgula
            print(fib[i]) 

if __name__ == "__main__":
    main()