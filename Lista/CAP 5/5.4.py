# Exercício 4 do Capítulo 5 das Listas de Linguagem de Programação - ECT3201

def calcular_bonificacao(medalhas, recorde_mundial, primeira_medalha_pais): # Função que calcula a bonificação com 3 parâmetros, medalhas, recorde_mundial e primeira_medalha_pais.
    bonificacao = 0 # Variável que armazena a bonificação inicialmente como 0, porque não temos nenhuma medalha.
    # Laço que percorre a lista de medalhas.
    for medalha in medalhas: # Para cada medalha na lista de medalhas. 
        if medalha.lower() == "ouro": # Se a medalha for de ouro.
            bonificacao += 50000 # Adiciona 50000 à bonificação.
        elif medalha.lower() == "prata": # Se a medalha for de prata.
            bonificacao += 30000 # Adiciona 30000 à bonificação.
        elif medalha.lower() == "bronze": # Se a medalha for de bronze.
            bonificacao += 10000 # Adiciona 10000 à bonificação.
    # Condição que verifica se o recorde mundial é sim.
    if recorde_mundial.lower() == "sim": # Se o recorde mundial for sim.
        bonificacao += 100000 # Adiciona 100000 à bonificação.
    if primeira_medalha_pais.lower() == "sim": # Se a primeira medalha do país for sim.
        bonificacao += 50000 # Adiciona 50000 à bonificação.

    return bonificacao # Retorna a bonificação.

entrada = input('').split(',') # Entrada que é separada por vírgula.

medalhas = entrada[:-2] # Medalhas é a entrada até o penúltimo elemento.
recorde_mundial = entrada[-2].strip() # Recorde mundial é o penúltimo elemento da entrada.
primeira_medalha_pais = entrada[-1].strip() # Primeira medalha do país é o último elemento da entrada.
print(calcular_bonificacao(medalhas, recorde_mundial, primeira_medalha_pais)) # Chama a função calcular_bonificacao com os parâmetros medalhas, recorde_mundial e primeira_medalha_pais e imprime o resultado.
# Uso de strip para remover espaços em branco no início e no final da string.