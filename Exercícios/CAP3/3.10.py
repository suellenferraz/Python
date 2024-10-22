# Exercício 10 do Capítulo 3 das Listas de Linguagem de Programação - ECT3201

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