# Exercício 8 do Capítulo 3 das Listas de Linguagem de Programação - ECT3201

# O uso de or em Python é um operador lógico que permite combinar múltiplas condições em uma única expressão. Se pelo menos uma das condições for verdadeira, a expressão total será considerada verdadeira.

def main():
    escolha = input().split() # Lê todas as entradas em uma única linha 
    # Condição para a escolha da pílula
    if escolha[0] == "Vermelha":  # Se a pílula escolhida for a vermelha
        if escolha[1] == "Sim" and escolha[2] == "Sim" and escolha[3] == "Sim": # Se todas as respostas forem "Sim" 
            print("Neo terá acesso a informações sobre a verdade.") # Neo terá acesso a informações sobre a verdade
        elif (escolha[1] == "Sim" and escolha[2] == "Não" and escolha[3] == "Sim") or \
             (escolha[1] == "Não" and escolha[2] == "Sim" and escolha[3] == "Sim"):
            print("A escolha é sua, Neo continua vivendo sua vida normal.")
    else: # Se a pílula escolhida for a azul
        print("Neo continua vivendo sua vida normal.")

if __name__ == "__main__":
    main()