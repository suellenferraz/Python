def manipular_string(s: str) -> list:
    """
    Realiza manipulações específicas em uma string.

    Parâmetros:
        s (str): A string de entrada.

    Retorna:
        list: Lista com os resultados das operações.
    """
    # Extrai o primeiro caractere
    primeiro_caractere = s[0]
    
    # Obtém o último caractere
    ultimo_caractere = s[-1]
    
    # Seleciona os três primeiros caracteres
    tres_primeiros = s[:3]
    
    # Captura os três últimos caracteres
    tres_ultimos = s[-3:]
    
    # Inverte a ordem dos caracteres
    invertida = s[::-1]
    
    # Remove as vogais minúsculas (sem usar join)
    vogais_minusculas = "aeiou"
    sem_vogais_minusculas = ""
    for c in s:
        if c not in vogais_minusculas:
            sem_vogais_minusculas += c  # Concatena apenas os caracteres que não são vogais
    
    # Compila os resultados em uma lista
    resultados = [
        primeiro_caractere,
        ultimo_caractere,
        tres_primeiros,
        tres_ultimos,
        invertida,
        sem_vogais_minusculas,
    ]
    
    return resultados

# Testes
texto = input()
print(manipular_string(texto))
