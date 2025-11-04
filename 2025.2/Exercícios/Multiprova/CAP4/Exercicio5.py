numeros = list(int,input().split(','))

numeros_impar = [x ** 2 for x in numeros if x % 2 != 0]