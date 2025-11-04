entrada = list(map(int, input().split(',')))

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
    resultados.append('X')
    
print(*resultados, sep=', ')
print(f'Quantidade de números inválidos: {n_invalidos}')