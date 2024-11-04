# Exercício 12 do Capítulo 2 das Listas de Linguagem de Programação - ECT3201

def main():
    aluno = {} # Dicionário
    # Coleta o os valores
    aluno["nome"] = input("") 
    aluno["matricula"] = input("")

    # Notas dos alunos para calcular a média das notas
    aluno["nota1"] = float(input(""))
    aluno["nota2"] = float(input(""))
    aluno["nota3"] = float(input(""))
    # Calcula a média
    media = (aluno["nota1"] + aluno["nota2"] + aluno["nota3"]) / 3

    print(f"Nome: {aluno['nome']}")
    print(f"Matrícula: {aluno['matricula']}")
    print(f"Média: {media:.2f}")  

if __name__ == "__main__":
    main()
