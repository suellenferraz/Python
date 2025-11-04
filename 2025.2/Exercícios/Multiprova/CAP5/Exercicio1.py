def ler_numeros():
  a = float(input())
  b = float(input())
  c = float(input())
  return a, b, c

def encontrar_menor_maior(a,b,c):
  menor = min(a,b,c)
  maior = max(a,b,c)
  return menor, maior

a, b, c = ler_numeros()
menor, maior = encontrar_menor_maior(a,b,c)

print(f'O menor número é: {menor}')
print(f'O maior número é: {maior}')