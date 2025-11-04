temperatura_celsius = list(map(float, input().split()))

calculo_temperatura = [
  (c * 9/5) + 32
  for c in temperatura_celsius
  if c >= 20.0
]

print(calculo_temperatura)