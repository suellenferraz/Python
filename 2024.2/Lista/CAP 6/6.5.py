import re

def limpar_dados_sensor(dados):
    # Remoção de caracteres especiais
    dados_limpos = re.sub(r'[^a-zA-Z0-9.:%°\s\-ãÃ]', '', dados)

    # Remoção de espaços extras
    dados_limpos = re.sub(r'\s+', ' ', dados_limpos)

    return dados_limpos

entrada = input()
saida = limpar_dados_sensor(entrada)
print(saida)
