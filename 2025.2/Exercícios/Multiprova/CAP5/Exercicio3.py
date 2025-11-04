def calcular_retangulo_info(comprimento:float, largura:float):
  area_triangulo = comprimento * largura
  perimento = 2 * ( comprimento + largura)
  return area_triangulo, perimento

comprimento = float(input())
largura = float(input())

area_triangulo, perimetro = calcular_retangulo_info(comprimento, largura)

print(f"A área do retângulo é: {area_triangulo:.2f}")
print(f"O perímetro do retângulo é: {perimetro:.2f}")