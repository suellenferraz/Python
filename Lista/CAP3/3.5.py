# Exercício 5 do Capítulo 3 das Listas de Linguagem de Programação - ECT3201
"""Utilizando tuplas, você deve receber as coordenadas de um retângulo no plano cartesiano, onde (x_min, y_min) representa o canto inferior esquerdo e (x_max, y_max) representa o canto superior direito. Além disso, você tem um ponto representado por um par de coordenadas (x, y).
Sua tarefa é escrever um programa que determine se o ponto está dentro, tocando na borda ou fora do retângulo. O programa deve imprimir uma mensagem na saída padrão indicando o resultado da verificação.
Veja o exemplo didático do desenho ASCII para o Teste 1:
O + representa os cantos do retângulo.
O . representa o ponto.
As coordenadas do retângulo são (x_min, y_min) = (1,1) e (x_max, y_max) = (6,6).
As coordenadas do ponto são (x, y) = (4,4)."""

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
