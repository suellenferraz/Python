# Exercício 10 do Capítulo 5 das Listas de Linguagem de Programação - ECT3201

def torre_de_hanoi(n, origem, auxiliar, destino): # Função que resolve o problema da Torre de Hanói.
    if n == 1: # Se houver apenas um disco.
        print(f'Mover disco de {origem} para {destino}') # Imprime a movimentação do disco.
    else: # Se não.
        torre_de_hanoi(n - 1, origem, destino, auxiliar) # Chama a função recursivamente para mover n-1 discos da origem para o auxiliar.
        print(f'Mover disco de {origem} para {destino}') # Imprime a movimentação do disco.
        torre_de_hanoi(n - 1, auxiliar, origem, destino) # Chama a função recursivamente para mover n-1 discos do auxiliar para o destino.
 
n, origem, auxiliar, destino = input().split(', ') # Lê o número de discos, a origem, o auxiliar e o destino separados por vírgula.
torre_de_hanoi(int(n), origem, auxiliar, destino) # Chama a função torre_de_hanoi com o número de discos, a origem, o auxiliar e o destino.

