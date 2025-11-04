numeros = list(map(int, input().split(',')))

numeros_primos = []

for n in numeros:
  if n >= 2:
    e_primo = True
    for i in range(2,n):
        if n % i == 0:
            e_primo = False
            break
    if e_primo:
        numeros_primos.append(n)

print(*numeros_primos, sep = ', ')