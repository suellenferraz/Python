import requests
import re

def explorar_wiki(url, palavra_chave):
    """
    Busca o conteúdo de um artigo da Wikipedia e realiza manipulações com base em uma palavra-chave.
    Args:
        url (str): URL do artigo da Wikipedia.
        palavra_chave (str): Palavra-chave para buscas e análises no conteúdo do artigo.
    Retorna:
        dict: Um dicionário contendo o número de ocorrências da palavra-chave, e o título do artigo.
    """
    try:
        # Fazer a requisição HTTP
        response = requests.get(url)

        # Verificar se a requisição foi bem-sucedida (status 200)
        if response.status_code != 200:
            return {
                "titulo": "Erro na requisição",
                "ocorrencias": 0
            }

        # Extrair o título do artigo
        titulo_match = re.search(r'<title>(.*?)</title>', response.text)
        titulo = titulo_match.group(1) if titulo_match else "Título não encontrado"

        # Normalizar a palavra-chave para busca case-insensitive
        palavra_chave_lower = palavra_chave.lower()

        # Contar ocorrências da palavra-chave em todo o conteúdo
        ocorrencias = len(re.findall(palavra_chave_lower, response.text.lower()))

        return {
            "titulo": titulo,
            "ocorrencias": ocorrencias
        }

    except requests.RequestException as e:
        return {
            "titulo": "Erro de Conexão",
            "ocorrencias": 0
        }

# Exemplo de uso
url, palavra_chave = input().split(",")
url = url.strip('"')
palavra_chave = palavra_chave.strip('"')
resultado = explorar_wiki(url, palavra_chave)
print(resultado)