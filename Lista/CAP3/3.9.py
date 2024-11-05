# Exercício 9 do Capítulo 3 das Listas de Linguagem de Programação - ECT3201
"""Você é um fotógrafo profissional. Durante um trabalho, você se depara com um lago cristalino cercado por imensas montanhas. Seu objetivo é capturar uma foto aérea épica do lago, utilizando um drone. Para garantir a melhor perspectiva, você precisa determinar a altura ideal de voo do drone. Para isso, será necessário saber a distância horizontal entre você e a margem do lago, bem como a altura vertical que deseja alcançar com o drone.
A hipotenusa, que representa a distância diagonal percorrida pelo drone, pode ser calculada utilizando o Teorema de Pitágoras: hipotenusa = √(cateto_adjacente² + cateto_oposto²).
Seu programa receberá como entrada, em metros, o comprimento do cateto adjacente e do cateto oposto, e calculará a hipotenusa correspondente."""

def main():
    # Uso do split() para transforma em uma string e em seguida o uso do map para fazer a conversão desses valores para float
    cateto_adjacente, cateto_oposto = map(float, input("").split()) 
    hipotenusa = (cateto_adjacente ** 2 + cateto_oposto ** 2) ** 0.5 # Teorema de Pitágoras 

    print(f"{hipotenusa:.2f} metros") # Uso do .2f para duas casas decimais

if __name__ == "__main__":
    main()