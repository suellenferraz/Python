'''
Crie um programa que lê um valor numérico N e que em seguida lê N números. Armazene esses números em uma lista. Em seguida, leia do usuário 3 números inteiros (OP, A e B). O primeiro número (OP) representa uma operação matemática (0 é soma, 1 é multiplicação) que deve ser realizada em cima dos dois números cujas posições (1 a N) na lista são A e B. O programa deve então apresentar a operação e seu resultado.

Exemplo

Qual o N? 5
Digite os valores:
10
20
30
40
50
Qual a op? 1
Qual o A? 2
Qual o B? 4
20 * 40 = 800
'''

N = int(input("Qual o N? "))
numeros = []

print("Digite os valores:")
for _ in range(N):
    valor = float(input())
    numeros.append(valor)
OP = int(input("Qual a op? "))
A = int(input("Qual o A? "))
B = int(input("Qual o B? "))
num_a = numeros[A - 1]
num_b = numeros[B - 1]
if OP == 0:
    resultado = num_a + num_b
    operacao = "+"
elif OP == 1:
    resultado = num_a * num_b
    operacao = "*"
print(f"{num_a:.0f} {operacao} {num_b:.0f} = {resultado:.0f}")