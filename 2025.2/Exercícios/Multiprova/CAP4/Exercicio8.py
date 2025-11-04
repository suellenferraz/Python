numeros = list(map(int, input().split(',')))

resultado = []

for x in numeros:
    if x % 2 != 0 and x > 5:
        resultado.append(x ** 3)
    elif x % 2 == 0 and x > 5:
        resultado.append(x ** 2)

print(resultado)