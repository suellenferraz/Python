'''
Escreva um programa que lê a quantidade dos alunos de uma turma. Em seguida, o programa deve ler os nomes de cada aluno e imprimí-los na ordem inversa.

Exemplo

Quantos nomes? 3
João
Paulo
Augusto
Você digitou:
Augusto
Paulo
João
'''

n = int(input("Quantos nomes? "))
nomes = [input() for _ in range(n)]
print("Você digitou:")
for nome in reversed(nomes):
    print(nome)