# Exercício 2 - Criando um padrão de moldura.

'''
1. Ter uma linha superior e inferior composta pelo caractere decorativo repetido.
2. O texto deve estar centralizado na moldura.
3. Deve haver um espaço entre o texto e o caractere decorativo nas laterais.
4. A largura total da moldura deve ser o comprimento do texto mais 4 caracteres (para os espaços e caracteres decorativos nas laterais).
'''

entrada, elemento_decorativo = input().split()

def criar_moldura(entrada, elemento_decorativo):
    largura_moldura = len(entrada) + 4
    linha_superior_inferior = elemento_decorativo * largura_moldura
    linha_texto = f"{elemento_decorativo} {entrada} {elemento_decorativo}"
    return f"{linha_superior_inferior}\n{linha_texto}\n{linha_superior_inferior}"

print(criar_moldura(entrada,elemento_decorativo))
