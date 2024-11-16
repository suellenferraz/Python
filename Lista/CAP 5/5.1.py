# Exercício 1 do Capítulo 5 das Listas de Linguagem de Programação - ECT3201

def ler_numeros(): # Função que lê os números
    num1, num2, num3 = map(float, input("").split(",")) # Lê os valores de entrada que no caso é 3 números e separar por vírgula com uso do split. O map é para transformar os valores em float.
    return num1, num2, num3 # Retorna os valores lidos. Return é uma palavra reservada que serve para retornar valores de uma função que no caso é a função ler_numeros.
def encontrar_menor_maior(num1, num2, num3): # 2º Função que encontra o menor e o maior número entre os 3 números
    menor = num1 # Inicializa a variável menor com o valor de num1
    maior = num1 # Inicializa a variável maior com o valor de num1
    # Aqui precisa ter condições devido a possibilidade de num1 ser o menor ou o maior número e o mesmo para num2 e num3.
    if num2 < menor: # Se num2 for menor que menor então menor recebe num2
        menor = num2 
    if num3 < menor: # Se num3 for menor que menor então menor recebe num3
        menor = num3

    if num2 > maior: # Se num2 for maior que maior então maior recebe num2
        maior = num2
    if num3 > maior: # Se num3 for maior que maior então maior recebe num3
        maior = num3

    return menor, maior 
# Exemplo de uso das funções
num1, num2, num3 = ler_numeros() # Chama a função ler_numeros e atribui os valores lidos para as variáveis num1, num2 e num3
menor, maior = encontrar_menor_maior(num1, num2, num3) # Chama a função encontrar_menor_maior e atribui os valores retornados para as variáveis menor e maior
# Aqui precisa ter condições para verificar se o menor e o maior são inteiros para não mostrar a saída com ponto flutuante.
if menor == int(menor): # Se menor for igual a menor inteiro então menor recebe menor inteiro
    menor = int(menor) 

if maior == int(maior): # Se maior for igual a maior inteiro então maior recebe maior inteiro
    maior = int(maior)
# Aqui imprime o menor e o maior número
print(f"O menor número é: {menor}")
print(f"O maior número é: {maior}")