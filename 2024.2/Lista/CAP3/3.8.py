# Exercício 8 do Capítulo 3 das Listas de Linguagem de Programação - ECT3201
"""Auxiliando o Hacker Neo a Desvendar a Verdade Sobre a Realidade.
História da Matrix: Neo, um hacker talentoso, vive uma vida dupla. No mundo que ele conhece, ele é um programador comum. Mas, e se existisse uma realidade escondida, uma verdade que ele nunca imaginou?
Após ser contatado por Morpheus, Neo se depara com uma escolha crítica: tomar a pílula vermelha e desvendar a verdade, ou tomar a pílula azul e continuar vivendo sua vida como sempre.
Fases do Programa:
Fase 1: A Escolha ● ●
Neo deve escolher entre a pílula vermelha e a pílula azul. A escolha é feita através de um input do usuário:
Se o usuário digitar “vermelha”, Neo avança para a fase 2.
Se o usuário digitar “azul”, Neo continua vivendo sua vida normal e o programa termina.

Fase 2: Desvendando a Realidade
Neo precisa questionar a realidade em que vive. Ele deve responder a três perguntas:
A realidade que você conhece é real? (Sim ou Não)
Existe uma realidade escondida? (Sim ou Não)
Você quer desvendar a verdade? (Sim ou Não)

Fase 3: Explorando a Verdade
Se Neo responder “Sim” a todas as perguntas da fase 2, ele terá acesso a informações sobre a verdade, e o programa termina com uma mensagem de sucesso.
Se Neo responder “Não” a qualquer uma das perguntas da fase 2, ele continua vivendo sua vida normal, e o programa termina com uma mensagem de que a escolha é dele."""

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