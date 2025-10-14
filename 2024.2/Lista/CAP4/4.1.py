# Exercício 1 do Capítulo 4 das Listas de Linguagem de Programação - ECT3201

# Classificação Etária: Desenvolva um programa que recebe várias idades de usuários na entrada, todas separadas por espaços. Para cada idade, o programa deve imprimir a categoria correspondente de acordo com a seguinte escala.
# Categoria
'''
Faixa Etária
Menor de idade = Menos de 13 anos
Adolescente = De 13 a 17 anos
Maior de idade = De 18 a 59 anos
Idoso = 60 anos ou mais
'''

def main():
    idades = input().split()  # Recebe uma lista de idades separadas por espaço 
    for idade in idades: # Loop que verifica a categoria de cada idade 
        idade = int(idade) # Converte a idade de string para inteiro 
        if idade < 13: # Verifica se a idade é menor que 13 
            print("Menor de idade") # Imprime "Menor de idade" se a idade for menor que 13 
        elif 13 <= idade <= 17: # Verifica se a idade está entre 13 e 17 
            print("Adolescente") # Imprime "Adolescente" se a idade estiver entre 13 e 17 
        elif 18 <= idade <= 59: # Verifica se a idade está entre 18 e 59 
            print("Maior de idade") # Imprime "Maior de idade" se a idade estiver entre 18 e 59 
        else: # Caso contrário 
            print("Idoso") # Imprime "Idoso" se a idade for 60 ou mais
if __name__ == "__main__":
    main()