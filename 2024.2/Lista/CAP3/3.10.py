# Exercício 10 do Capítulo 3 das Listas de Linguagem de Programação - ECT3201
"""Um artesão está trabalhando em duas peças: um cone de metal e um paralepípedo de madeira. Para ajudá-lo em seu projeto, você precisa desenvolver um programa que receba as informações de dimensões em cm desses objetos e calcule seus volumes e massas.
Receber na entrada as seguintes informações para o cone: Altura e Raio.
Em seguida, receber as informações para o paralepípedo: Altura, Largura e Comprimento.
Calcule a massa de cada objeto, considerando que a densidade do metal é de 8 g/cm³ e a densidade da madeira é de 0,5 g/cm³. Qual dos dois objetos, cone ou paralepípedo, é mais pesado? Considere que eles possuem o mesmo peso se a diferença entre as massas for menor do que 5g.
Lembre da fórmula do volume do cone e do paralepípedo. Volume do cone = (1/3) * π * r² * h. Volume do paralelepípedo = h * l * c."""

def main():
     # Uso do split() para transforma em uma string e em seguida o uso do map para fazer a conversão desses valores para float
    altura_cone, raio_cone, altura_paralelepipedo, largura_paralelepipedo, comprimento_paralelepipedo = map(float, input("").split())
    # Volume do cone (tinha 5 no final, coloquei um 6, devido que não tava arredondando)
    volume_cone = (1 / 3) * 3.1416 * (raio_cone ** 2) * altura_cone
    # Volume do paralelepipedo
    volume_paralelepipedo = altura_paralelepipedo * largura_paralelepipedo * comprimento_paralelepipedo
    # Massas
    densidade_metal = 8  
    densidade_madeira = 0.5  

    massa_cone = volume_cone * densidade_metal
    massa_paralelepipedo = volume_paralelepipedo * densidade_madeira
    # Comparação quem é + pesado ou não
    if massa_cone - massa_paralelepipedo < 5 and massa_cone - massa_paralelepipedo > -5:
        print(f"O paralepípedo e o cone possuem o mesmo peso.")
    elif massa_cone > massa_paralelepipedo:
        print(f"O cone é mais pesado com {round(massa_cone, 2):.2f}g.") # Usei a função round para fazer o arrendodamento, devido tá dando erro.
    else:
        print(f"O paralelepípedo é mais pesado com {round(massa_paralelepipedo, 2):.2f}g.")

if __name__ == "__main__":
    main()