# Calcular a distância entre dois pontos

def main():
    # Recebendo os valores de x1, y1, x2, y2
    x1, y1, x2, y2 = map(float, input("Digite os valores de x1, y1, x2, y2: ").split())
    # Calculando a distância entre os pontos
    distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    print(f"A distância entre os pontos é {distancia:.2f}.")
if __name__ == "__main__":
    main()