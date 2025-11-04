numeros = list(map(int, input().split()))

positivo = 0
zero = 0
soma_positivo = 0

for numero in numeros:
    if numero > 0:
        positivo += 1
        soma_positivo += numero
    elif numero == 0:
        zero += 1
        
print(f'Quantidade de números positivos: {positivo}')
print(f'Quantidade de zeros: {zero}')
print(f'Soma dos números positivos: {soma_positivo}')