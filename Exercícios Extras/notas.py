# Calcular as notas de uma turma, tirar a média e verificar se estava em recuperação, reprovado ou aprovado.

def main():
    # Recebendo as notas
    nota1, nota2, nota3 = map(float, input("Digite as notas: ").split()) # map() converte as strings para números reais
    # Calculando a média
    media = (nota1 + nota2 + nota3) / 3
    # Verificando se a média é maior ou igual a 7
    if media >= 7:
        print(f"Aluno aprovado com média {media:.2f}.")
    # Verificando se a média é maior ou igual a 5 e menor que 7
    elif media >= 5:
        print(f"Aluno em recuperação com média {media:.2f}.")
    # Verificando se a média é menor que 5
    else:
        print(f"Aluno reprovado com média {media:.2f}.")
if __name__ == "__main__":
    main()

# Caso eu tenho os valores de notas sejam 9,0 , 6,0 e 5,0,.
def main():
    # Recebendo as notas
    nota1, nota2, nota3 = 9.0, 6.0, 5.0
    # Calculando a média
    media = (nota1 + nota2 + nota3) / 3
    # Verificando se a média é maior ou igual a 7
    if media >= 7:
        print(f"Aluno aprovado com média {media:.2f}.")
    # Verificando se a média é maior ou igual a 5 e menor que 7
    elif media >= 5:
        print(f"Aluno em recuperação com média {media:.2f}.")
    # Verificando se a média é menor que 5
    else:
        print(f"Aluno reprovado com média {media:.2f}.")
if __name__ == "__main__":
    main()