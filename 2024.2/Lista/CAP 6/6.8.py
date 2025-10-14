def gerar_prompt(titulo, descricao):
    """
    Gera um prompt formatado para modelos de IA.

    Args:
        titulo (str): O título do prompt.
        descricao (str): Uma breve descrição do contexto ou objetivo.

    Retorna:
        str: O prompt formatado.
    """
    return f"=== TÍTULO ===\n{titulo}\n\nDescrição:\n{descricao}"

titulo, descricao = input().split(",")
#titulo = titulo.strip('"')
#descricao = descricao.strip('"')
print(gerar_prompt(titulo, descricao))