# Exercício 3 do Capítulo 5 das Listas de Linguagem de Programação - ECT3201

import math # Importa a biblioteca math

def calcular_area(): # Função que calcula a área
    opcao = int(input()) # Lê a opção que é um número inteiro
    
    # Aqui precisa ter condições para verificar se a opção é 1, 2 ou 3 para calcular a área do triângulo, círculo ou retângulo.
    if opcao == 1:
        base = float(input()) # Lê a base
        altura = float(input()) # Lê a altura
        area = area_triangulo(base, altura) # Chama a função area_triangulo
        print(f'A área do triângulo é: {area:.2f}') # Imprime a área do triângulo com duas casas decimais
    
    elif opcao == 2: 
        raio = float(input()) 
        area = area_circulo(raio) # Chama a função area_circulo
        print(f'A área do círculo é: {area:.2f}') # Imprime a área do círculo com duas casas decimais
    
    elif opcao == 3:
        comprimento = float(input())
        largura = float(input())
        area = area_retangulo(comprimento, largura) # Chama a função area_retangulo
        print(f'A área do retângulo é: {area:.2f}') # Imprime a área do retângulo com duas casas decimais
        
    else:
        print("Programa encerrado.") # Se a opção não for 1, 2 ou 3, imprime "Programa encerrado."

# Funções para calcular a área do triângulo, círculo e retângulo, elas recebem os parâmetros base, altura, raio, comprimento e largura e retornam a área do triângulo, círculo e retângulo, respectivamente.
def area_triangulo(base,altura): 
    area_triangulo = base * altura/2
    return area_triangulo 

def area_circulo(raio):
    area_circulo = math.pi * raio**2 
    return area_circulo

def area_retangulo(comprimento,largura):
    area_retangulo = comprimento * largura
    return area_retangulo

calcular_area() # Chama a função calcular_area