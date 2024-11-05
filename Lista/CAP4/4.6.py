# Exercício 6 do Capítulo 4 das Listas de Linguagem de Programação - ECT3201

# Jogo da Adivinhação (Jogador vs Computador): O objetivo é desenvolver um jogo interativo de adivinhação de números no qual o jogador compete contra o computador. O jogo deve seguir as seguintes regras:
""" No início do jogo, o programa deve gerar um número aleatório secreto entre 1 e 100. Este será o número que o jogador e o computador tentarão adivinhar.
Tanto o jogador quanto o computador têm um número limitado de tentativas para adivinhar o número. Por exemplo, pode-se limitar a 20 tentativas.
Em cada rodada, o jogador e o computador fazem um palpite. O programa deve então fornecer uma dica para ambos, indicando se o número secreto é maior ou menor que os palpites.
Se o jogador ou o computador adivinhar o número corretamente, o programa deve parabenizá-lo e informar o número de tentativas que foram necessárias para adivinhar o número. Se ambos adivinharem o número na mesma rodada, o jogo termina em empate.
Se o jogador e o computador esgotarem todas as suas tentativas sem adivinhar o número, o programa deve informar que o jogo terminou e revelar o número secreto. """

# Questão dar erro timeout (não sei o motivo) na plataforma Lop

def main():
    import random # Importa a biblioteca random
    print("Bem-vindo ao jogo da adivinhação!") # Exibe uma mensagem de boas-vindas
    print("O número secreto está entre 1 e 100.") # Exibe a faixa de números do número secreto
    print("Você tem 20 tentativas para adivinhar o número secreto.") # Exibe o número de tentativas disponíveis
    print("Boa sorte!") # Exibe uma mensagem de boa sorte
    numero_secreto = random.randint(1, 100) # Gera um número aleatório secreto entre 1 e 100
    tentativas = 0  # Inicializa o contador de tentativas
    while tentativas < 20:  # Loop que simula o jogo da adivinhação
        tentativas += 1 # Incrementa o contador de tentativas
        palpite = int(input("Digite seu palpite: "))    # Recebe o palpite do jogador
        if palpite == numero_secreto:   # Verifica se o palpite do jogador é igual ao número secreto
            print(f"Parabéns! Você adivinhou o número secreto em {tentativas} tentativas!") # Exibe uma mensagem de parabéns
            break   # Encerra o loop
        elif palpite < numero_secreto:  # Verifica se o palpite do jogador é menor que o número secreto
            print("O número secreto é maior.")  # Exibe uma dica para o jogador
        else:   # Caso contrário
            print("O número secreto é menor.")  # Exibe uma dica para o jogador
    print(f"O número secreto era {numero_secreto}.")    # Exibe o número secreto
    print("Fim de jogo!")   # Exibe uma mensagem de fim de jogo
if __name__ == "__main__":
    main()