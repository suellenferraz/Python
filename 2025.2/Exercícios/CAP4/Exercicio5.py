'''
entrada = list(map(int,input().split(',')))

n_invalidos = 0
lista_resultados = []

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
    return fatorial(n)

for n in entrada:
    if 0 <= n < 15:
        lista_resultados.append(fatorial(n))
    else:
        n_invalidos += 1
        lista_resultados.append('X')

print(lista_resultados)
print(f'Quantidade de números inválidos: {n_invalidos}')
'''

entrada = list(map(float, input().split(',')))

n_invalidos = 0
resultados = []

def fatorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * fatorial(n - 1)

for n in entrada:
  if 0 <= n < 15:
    resultados.append(fatorial(n))
  else:
    n_invalidos += 1
    resultados.append(fatorial(n))
    
print(resultados)
print(f'Quantidade de números inválidos: {n_invalidos}')