# Exercício 7 do Capítulo 3 das Listas de Linguagem de Programação - ECT3201
"""Você é um biólogo trabalhando em um parque natural e está encarregado de monitorar três espécies de aves migratórias. Cada espécie tem um conjunto de ilhas preferidas para nidificação durante a temporada de migração. As preferências das espécies são as seguintes:
Espécie 1: Prefere as ilhas com IDs de 1 a 10.
Espécie 2: Prefere as ilhas com IDs de 6 a 17.
Algumas ilhas são compartilhadas entre as espécies, o que pode levar à competição por recursos. Seu trabalho é identificar quais ilhas são compartilhadas para implementar medidas de conservação. Dessa forma, dada uma entrada do usuário correspondente ao ID de uma das ilhas, verifique se essa ilha específica é uma área de competição ou se é exclusiva de uma das espécies."""

def main():
    # Utilizei o set e o range para facilitar o conjunto das ilhas
    especie1 = set(range(1, 11))  # Conjunto de ilhas preferidas pela Espécie 1 (ilhas 1 a 10)
    especie2 = set(range(6, 18))  # Conjunto de ilhas preferidas pela Espécie 1 (ilhas 1 a 17)
    ilha = int(input())  
    # Verificar se os conjuntos é compartilhado ou exclusivo através do operador "in".
    if ilha in especie1 and ilha in especie2:
        print(f"Ilha {ilha} é compartilhada entre espécie(s):1 2.")
    elif ilha in especie1:
        print(f"Ilha {ilha} é exclusiva da Espécie 1.\nPortanto, não é compartilhada com outras espécies.")
    elif ilha in especie2:
        print(f"Ilha {ilha} é exclusiva da Espécie 2.\nPortanto, não é compartilhada com outras espécies.")
    else:
        print(f"Ilha {ilha} não está nas preferências das espécies.")
    
if __name__ == "__main__":
    main()