# Exercício 9 do Capítulo 4 das Listas de Linguagem de Programação - ECT3201

#  Loteria de 5 números: Desenvolva um programa que simule uma loteria onde são sorteados 5 números distintos entre 1 e 50. O programa deve gerar aleatoriamente jogos de 5 números até que um jogo corresponda exatamente à combinação sorteada. O objetivo é determinar quantos jogos são necessários até que haja um ganhador. Siga as instruções a seguir:
""" Receba na entrada um inteiro correspondente à semente para geração pseudoaleatória de números.
Gere uma combinação vencedora de 5 números únicos entre 1 e 50 usando random.sample.
Converta a combinação vencedora em um conjunto (set) para facilitar a comparação.
Crie um loop que simule jogos de 5 números únicos entre 1 e 50, também usando random.sample.
Após cada jogo, converta a combinação de números gerada em um conjunto (set) e verifique se ela corresponde à combinação vencedora.
Conte o número de jogos realizados até que um jogo corresponda exatamente à combinação vencedora.
Exiba o número total de jogos necessários para encontrar um ganhador. """

def main():
    import random # Importa a biblioteca random
    random.seed(int(input())) # Define a semente para geração pseudoaleatória de números
    vencedor = set(random.sample(range(1, 51), 5)) # Gera uma combinação vencedora de 5 números únicos entre 1 e 50
    jogos = 0 # Inicializa o contador de jogos
    while True: # Loop que simula jogos de 5 números únicos entre 1 e 50
        jogos += 1 # Incrementa o contador de jogos realizados até que um jogo corresponda exatamente à combinação vencedora
        if set(random.sample(range(1, 51), 5)) == vencedor: # Verifica se a combinação de números gerada corresponde à combinação vencedora
            break # Encerra o loop
    print(f"Número de jogos necessários: {jogos}") # Exibe o número total de jogos necessários para encontrar um ganhador
if __name__ == '__main__':
    main()