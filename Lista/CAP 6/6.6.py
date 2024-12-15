def gerar_relatorio(nome_experimento, valores_medidos, valor_esperado):
    # Calcula a média dos valores medidos
    media = sum(valores_medidos) / len(valores_medidos)
    # Calcula a diferença absoluta entre a média e o valor esperado
    diferenca = abs(media - valor_esperado)
    # Gera o relatório formatado com f-strings
    relatorio = (
        f"Experimento: {nome_experimento}\n"
        f"Média dos valores medidos: {media:.2f}\n"
        f"Diferença em relação ao valor esperado: {diferenca:.2f}"
    )
    return relatorio

entrada = input().split(",")
nome_experimento = entrada[0].strip()
valores_medidos = [float(valor) for valor in entrada[1].split()]
valor_esperado = float(entrada[2].strip())

print(gerar_relatorio(nome_experimento, valores_medidos, valor_esperado))
