# Exercício 7 do Capítulo 3 das Listas de Linguagem de Programação - ECT3201

def main():
    # Utilizei o set e o range para facilitar o conjunto das ilhas
    especie1 = set(range(1, 11))  # Conjunto de ilhas preferidas pela Espécie 1 (ilhas 1 a 10)
    especie2 = set(range(6, 18))  # Conjunto de ilhas preferidas pela Espécie 1 (ilhas 1 a 17)
    ilha = int(input())  
    # Verificar se os conjuntos é compartilhado ou exclusivo através do operador "in".
    if ilha in especie1 and ilha in especie2:
        print(f"Ilha {ilha} é compartilhada entre espécie(s):1 2.")
    elif ilha in especie1:
        print(f"Ilha {ilha} é exclusiva da Espécie 1.\nPortanto, não é compartilhada com outras espécies.")
    elif ilha in especie2:
        print(f"Ilha {ilha} é exclusiva da Espécie 2.\nPortanto, não é compartilhada com outras espécies.")
    else:
        print(f"Ilha {ilha} não está nas preferências das espécies.")
    
if __name__ == "__main__":
    main()