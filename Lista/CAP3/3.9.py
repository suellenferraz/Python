# Exercício 9 do Capítulo 3 das Listas de Linguagem de Programação - ECT3201

def main():
    # Uso do split() para transforma em uma string e em seguida o uso do map para fazer a conversão desses valores para float
    cateto_adjacente, cateto_oposto = map(float, input("").split()) 
    hipotenusa = (cateto_adjacente ** 2 + cateto_oposto ** 2) ** 0.5 # Teorema de Pitágoras 

    print(f"{hipotenusa:.2f} metros") # Uso do .2f para duas casas decimais

if __name__ == "__main__":
    main()