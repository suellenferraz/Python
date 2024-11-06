# A sequência de Fibonacci é uma sequência onde cada termo pode ser calculado a partir dos dois termos anteriores. Por definição, o primeiro termo da sequência é 0 e o segundo é 1. Assim, os próximos termos da sequência são 1, 2, 3 e 5. Escreva um programa que recebe um número inteiro positivo n e imprime os n primeiros termos da sequência de Fibonacci.
# Utilize While para resolver o problema.

def main():
    n = int(input("")) # Recebendo o valor de n 
    a, b = 0, 1 # Definindo os valores de a e b como 0 e 1
    i = 0 # Definindo o contador i como 0 
    while i < n: # Enquanto i for menor que n 
        print(a, end=" ") # Imprimindo o valor de a 
        a, b = b, a + b # Calculando os valores de a e b 
        i += 1 # Incrementando o contador i
if __name__ == "__main__":
    main()