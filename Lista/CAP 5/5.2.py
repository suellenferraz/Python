# Exercício 2 do Capítulo 5 das Listas de Linguagem de Programação - ECT3201

def ler_dados(): # função que lê os dados de entrada
    peso, altura = map(float, input("").split(",")) # Lê os valores de entrada que no caso é 2 números e separar por vírgula com uso do split. O map é para transformar os valores em float.
    return peso, altura # Retorna os valores de peso e altura
    
def calcular_imc(peso,altura): # Função que calcula o IMC
    imc = peso/(altura*altura) # Fórmula do IMC que é o peso dividido pela altura ao quadr
    return imc # Retorna o valor do IMC
    
def classificar_imc(imc): # Função que classifica o IMC
    if imc < 18.5: 
        classificacao = "Abaixo do peso"
    elif 18.5 <= imc < 25.0: 
        classificacao = "Peso normal"
    elif 25.0 <= imc < 30.0:
        classificacao = "Sobrepeso"
    elif 30.0 <= imc < 35.0:
        classificacao = "Obesidade grau 1"
    elif 35.0 <= imc < 40.0:
        classificacao = "Obesidade grau 2"
    else: 
        classificacao = "Obesidade grau 3"
    return classificacao

# Exemplo de uso das funções
peso, altura = ler_dados() # Chama a função ler_dados e atribui os valores lidos para as variáveis peso e altura
imc = calcular_imc(peso,altura) # Chama a função calcular_imc e atribui o valor retornado para a variável imc
classificacao = classificar_imc(imc) # Chama a função classificar_imc e atribui o valor retornado para a variável classificacao
print(f'Seu IMC é {imc:.2f} - Classificação: {classificacao}') # Imprime o valor do IMC com 2 casas decimais e a classificação do IMC