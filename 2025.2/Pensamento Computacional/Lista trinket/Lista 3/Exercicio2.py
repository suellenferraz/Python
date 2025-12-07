'''
Um treinador de voleibol gostaria de manter estatísticas sobre sua equipe. A cada jogo, seu auxiliar anota quantas tentativas de saques, bloqueios e ataques cada um de seus jogadores fez, bem como quantos desses saques, bloqueios e ataques tiveram sucesso (resultaram em pontos). Seu programa deve mostrar qual o percentual de saques, bloqueios e ataques do time todo tiveram sucesso.

Formato de entrada

A primeira entrada é o número de jogadores N (N >= 1). Em seguida, para cada jogador, deve-se se ler uma linha com as seguintes informações: nome do jogador, os valores S, B e A, representam a quantidade de tentativas de saques, bloqueios e ataques; os valores S1, B1 e A1, representando o número de saques, bloqueios e ataques deste jogador que tiveram sucesso.

Lembre-se de usar LISTA para guardar os valores de cada jogador.

Formato de saída

A saída deve mostrar o percentual total de saques, bloqueios e ataques do time todo que resultaram em pontos, conforme mostrado no exemplo.

Exemplo

Quantidade de jogadores? 3
Digite os dados para cada jogador:
Renan 10 20 12 1 10 9
Jonas 8 7 1 2 7 0
Edson 3 3 3 1 2 3
As estatísticas do jogo são as seguintes:
Pontos de Saque: 19.05 %
Pontos de Bloqueio: 63.33 %
Pontos de Ataque: 75.00 %
'''

n = int(input("Quantidade de jogadores? "))
print("Digite os dados para cada jogador:")
total_saques = total_saques_sucesso = 0
total_bloqueios = total_bloqueios_sucesso = 0
total_ataques = total_ataques_sucesso = 0

for _ in range(n):
    dados = input().split()
    nome = dados[0]
    S, B, A = map(int, dados[1:4])
    S1, B1, A1 = map(int, dados[4:7])
    
    total_saques += S
    total_saques_sucesso += S1
    total_bloqueios += B
    total_bloqueios_sucesso += B1
    total_ataques += A
    total_ataques_sucesso += A1
percentual_saques = (total_saques_sucesso / total_saques * 100) if total_saques > 0 else 0
percentual_bloqueios = (total_bloqueios_sucesso / total_bloqueios * 100) if total_bloqueios > 0 else 0
percentual_ataques = (total_ataques_sucesso / total_ataques * 100) if total_ataques > 0 else 0
print("As estatísticas do jogo são as seguintes:")
print(f"Pontos de Saque: {percentual_saques:.2f} %")
print(f"Pontos de Bloqueio: {percentual_bloqueios:.2f} %")
print(f"Pontos de Ataque: {percentual_ataques:.2f} %")