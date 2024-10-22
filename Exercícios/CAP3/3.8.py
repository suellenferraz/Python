# Exercício 8 do Capítulo 3 das Listas de Linguagem de Programação - ECT3201

# Questão precisa de correção

def main():
    usuario = input("").lower()
    real = input("A realidade que você conhece é real?").lower()
    escondida = input("Existe uma realidade escondida?").lower()
    verdade = input("Você quer desvendar a verdade?").lower()


    # Fase 1 
    if usuario == "vermelha" and real == "sim" and escondida == "sim" and verdade == "sim":
        print("Neo terá acesso a informações sobre a verdade.")
    else:
        print("A escolha é sua, Neo continua vivendo sua vida normal.")
    if usuario == "azul":
        print("Neo continua sua vida normal.")
        


if __name__ == "__main__":
    main()