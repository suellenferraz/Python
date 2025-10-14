def analisar_texto(frase: str, palavra_alvo:str) -> str:
    # Normalizar as strings para análise insensível a maiúsculas/minúsculas
    frase_lower = frase.lower()
    palavra_alvo_lower = palavra_alvo.lower()

    # Verificar se a palavra-alvo está presente
    presente = palavra_alvo_lower in frase_lower

    # Contar o número de ocorrências
    ocorrencias = frase_lower.count(palavra_alvo_lower)

    # Encontrar a posição da primeira ocorrência
    posicao = frase_lower.find(palavra_alvo_lower)

    # Formatar a saída
    resultado = (
        f'A palavra "{palavra_alvo}" está presente: {"Sim" if presente else "Não"}\n'
        f'Número de ocorrências: {ocorrencias}\n'
        f'Posição da primeira ocorrência: {posicao}'
    )

    return resultado

# Testes
frase, palavra = input().split(",")
print(analisar_texto(frase, palavra))