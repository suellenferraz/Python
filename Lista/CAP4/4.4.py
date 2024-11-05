# Exercício 4 do Capítulo 4 das Listas de Linguagem de Programação - ECT3201

# Análise de Desempenho de uma Turma com até 100 Alunos: Analise o desempenho de uma turma com até 100 alunos em uma disciplina de linguagem de programação. Seu programa deve receber como entrada uma lista de até 100 números entre 0 e 10, representando as notas finais de cada aluno.
""" Para cada nota na lista, o programa deve: 
Adicionar a nota à uma soma total (para posterior cálculo da média da turma).
Verificar se a nota é maior ou igual a 5. Se for, incrementar o contador de alunos aprovados.
Se a nota for menor que 5, incrementar o contador de alunos reprovados.
Após processar todas as notas, o programa deve calcular e imprimir as seguintes informações: Número de Alunos Aprovados, Número de Alunos Reprovados e Média da Turma.
"""


def main():
    notas = input().split(',') # Recebe uma lista de notas separadas por vírgula e espaço
    soma = 0 # Inicializa a variável soma como 0 
    aprovados = 0 # Inicializa o contador de alunos aprovados
    reprovados = 0 # Inicializa o contador de alunos reprovados

    for nota in notas: # Loop que processa cada nota na lista de notas
        nota = float(nota) # Converte a nota de string para float 
        soma += nota # Adiciona a nota à soma total
        if nota >= 5: # Verifica se a nota é maior ou igual a 5 
            aprovados += 1 # Incrementa o contador de alunos aprovados 
        else: # Caso contrário 
            reprovados += 1 # Incrementa o contador de alunos reprovados 

    print(f'Número de Alunos Aprovados: {aprovados}') # Imprime o número de alunos aprovados
    print(f'Número de Alunos Reprovados: {reprovados}') # Imprime o número de alunos reprovados
    print(f'Média da Turma: {soma/len(notas):.2f}') # Imprime a média da turma com duas casas decimais
if __name__ == '__main__':
    main()