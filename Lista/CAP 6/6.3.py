import re

def busca_palavras_chave(texto, palavras_chave):
    # Converte o texto para minúsculas
    texto = texto.lower()
    
    # Inicializa o dicionário de resultados
    resultados = {palavra: 0 for palavra in palavras_chave}
    
    # Conta as ocorrências de cada palavra-chave
    for palavra in palavras_chave:
        # Usa expressão regular para encontrar palavras completas
        padrao = r'\b' + re.escape(palavra.lower()) + r'\b'
        contagem = len(re.findall(padrao, texto))
        resultados[palavra] = contagem
    
    return resultados

# Lê a entrada
entrada = input()
texto, *palavras_chave = entrada.split(",")
palavras_chave = [palavra.strip() for palavra in palavras_chave]

# Chama a função e imprime o resultado
resultado = busca_palavras_chave(texto, palavras_chave)
print(resultado)