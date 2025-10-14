# Exercício 4 do Capítulo 2 das Listas de Linguagem de Programação - ECT3201
"""Faça um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. O IMC é calculado dividindo-se o peso da pessoa pela sua altura ao quadrado. O IMC é uma medida da relação entre o peso e a altura de uma pessoa. O programa deve imprimir o IMC da pessoa."""

def main():
    peso = float(input(""))
    altura = float(input(""))
    imc = (peso/(altura**2)) # Calcular o IMC 
    
    # Classificação do IMC
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif 18.5 <= imc < 25.0: # Optei por utilizar elif, porque ele permite testar várias condições em sequência.
        classificacao = "Saudável"
    elif 25.0 <= imc < 30.0:
        classificacao = "Sobrepeso"
    elif 30.0 <= imc < 35.0:
        classificacao = "Obesidade grau I"
    elif 35.0 <= imc < 40.0:
        classificacao = "Obesidade grau II"
    else: # O else é o último bloco de uma cadeia de condições e será executado apenas se nenhuma das condições anteriores for verdadeira. Ele não verifica nenhuma condição.
        classificacao = "Obesidade grau III"

    print(f"Seu IMC é {imc:.2f} ({classificacao}).") # Aqui utiliza o fstring e o ".2f" para ter apenas 2 casas decimais após a vírgula.
    
if __name__ == "__main__":
    main()