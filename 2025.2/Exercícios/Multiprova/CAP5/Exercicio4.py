def contar_pares(numeros):
    return sum(1 for n in numeros if n % 2 == 0)

def contar_impares(numeros):
    return sum(1 for n in numeros if n % 2 != 0)

def contar_positivos(numeros):
    return sum(1 for n in numeros if n > 0)

def contar_negativos(numeros):
    return sum(1 for n in numeros if n < 0)

entrada = input().split(',')
numeros = [int(n) for n in entrada]

pares = contar_pares(numeros)
impares = contar_impares(numeros)
positivos = contar_positivos(numeros)
negativos = contar_negativos(numeros)

print(f'Quantidade de números pares: {pares}')
print(f'Quantidade de números ímpares: {impares}')
print(f'Quantidade de números positivos: {positivos}')
print(f'Quantidade de números negativos: {negativos}')