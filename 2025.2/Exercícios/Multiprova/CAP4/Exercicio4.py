palavras = list(input().split())

palavras_pares = [palavra.upper() for palavra in palavras if len(palavra) % 2 == 0]

print(palavras_pares)