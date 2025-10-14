# Exercício 8 do Capítulo 5 das Listas de Linguagem de Programação - ECT3201

def fibonacci(n): # Função que calcula o n-ésimo termo da sequência de Fibonacci.
    if n == 0: # Se n for igual a 0.
        return 0 # Retorna 0.
    if n == 1: # Se n for igual a 1.
        return 1 # Retorna 1.
    return fibonacci(n - 1) + fibonacci(n - 2) # Retorna a soma do n-1-ésimo termo com o n-2-ésimo termo.

def soma_recursiva(lista): # Função que calcula a soma dos elementos de uma lista de forma recursiva.
    if not lista: # Se a lista estiver vazia.
        return 0  # Retorna 0.
    return lista[0] + soma_recursiva(lista[1:]) # Retorna o primeiro elemento da lista somado com a chamada recursiva da função com o restante da lista.
 
lista = list(map(int, input().split(','))) # Lê a lista de números separados por vírgula e converte para inteiros.
fibonacci_lista = [fibonacci(i) for i in lista] # Cria uma lista com os n-ésimos termos da sequência de Fibonacci para cada número da lista.
print(soma_recursiva(fibonacci_lista)) # Chama a função soma_recursiva com a lista de n-ésimos termos da sequência de Fibonacci e imprime o resultado.