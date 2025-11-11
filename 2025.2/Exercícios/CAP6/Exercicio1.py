# Exercício 1 - Manipulação de strings.
'''
1. Extrai o primeiro caractere da string.
2. Obtém o último caractere da string.
3. Seleciona os três primeiros caracteres da string.
4. Captura os três últimos caracteres da string.
5. Inverte a ordem dos caracteres na string.
6. Remove apenas as vogais minúsculas (a, e, i, o, u) da string, mantendo as vogais maiúsculas e todos os outros caracteres.
'''

entrada = input()

def manipular_string(entrada):
    primeiro_caractere = entrada[0]
    ultimo_caractere = entrada[-1]
    tres_primeiros = entrada[:3]
    tres_ultimos = entrada[-3:]
    string_invertida = entrada[::-1]
    vogais_minusculas = 'aeiou'
    string_sem_vogais = ''
    for char in entrada:
        if char not in vogais_minusculas:
            string_sem_vogais += char
    return [primeiro_caractere, ultimo_caractere, tres_primeiros, tres_ultimos, string_invertida, string_sem_vogais]

print(manipular_string(entrada))
