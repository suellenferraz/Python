# Exercício 5 do Capítulo 3 das Listas de Linguagem de Programação - ECT3201

def main():
    # Recebe as coordenadas do retângulo e do ponto como entrada com o .split()
    x_min, y_min, x_max, y_max, x, y = map(int, input().split())

    # Define as tuplas para o retângulo e o ponto
    retangulo_inferior_esquerdo = (x_min, y_min)
    retangulo_superior_direito = (x_max, y_max)
    ponto = (x, y)

    # Verifica se o ponto está dentro, na borda ou fora do retângulo
    if (retangulo_inferior_esquerdo[0] < ponto[0] < retangulo_superior_direito[0] and retangulo_inferior_esquerdo[1] < ponto[1] < retangulo_superior_direito[1]):
        print("O ponto está dentro do retângulo.")
    elif (ponto[0] == retangulo_inferior_esquerdo[0] or ponto[0] == retangulo_superior_direito[0]) and (retangulo_inferior_esquerdo[1] <= ponto[1] <= retangulo_superior_direito[1]) or (ponto[1] == retangulo_inferior_esquerdo[1] or ponto[1] == retangulo_superior_direito[1]) and (retangulo_inferior_esquerdo[0] <= ponto[0] <= retangulo_superior_direito[0]):
        print("O ponto está tocando a borda do retângulo.")
    else:
        print("O ponto está fora do retângulo.")

if __name__ == "__main__":
    main()
