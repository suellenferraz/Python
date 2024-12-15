def criar_moldura(texto, caractere):
    # Calcula a largura total da moldura
    largura_total = len(texto) + 4

    # Cria a linha superior e inferior da moldura
    linha_superior_inferior = caractere * largura_total

    # Cria a linha do meio com o texto centralizado
    linha_meio = f"{caractere} {texto} {caractere}"

    # Imprime a moldura
    print(linha_superior_inferior)
    print(linha_meio)
    print(linha_superior_inferior)

# Leitura da entrada do usuário
texto, caractere = input().split(',')

# Remove espaços extras das entradas
texto = texto.strip()
caractere = caractere.strip()

# Cria a moldura com os valores fornecidos pelo usuário
criar_moldura(texto, caractere)