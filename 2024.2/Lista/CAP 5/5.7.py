# Exercício 7 do Capítulo 5 das Listas de Linguagem de Programação - ECT3201

def soma_recursiva(lista): # Função que calcula a soma dos elementos de uma lista de forma recursiva.
    if not lista: # Se a lista estiver vazia.
        return 0 # Retorna 0.
    return lista[0] + soma_recursiva(lista[1:]) # Retorna o primeiro elemento da lista somado com a chamada recursiva da função com o restante da lista.

lista = list(map(int, input().split(','))) # Lê a lista de números separados por vírgula e converte para inteiros.
print(soma_recursiva(lista)) # Chama a função soma_recursiva com a lista e imprime o resultado.