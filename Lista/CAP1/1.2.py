# Exercício 2 do Capítulo 1 das Listas de Linguagem de Programação - ECT3201
# Neste exercício, você deve ler duas entradas: o nome de um aluno e sua matrícula. Em seguida, exiba uma mensagem de boas-vindas formatada com esses dados.

def main():
    nome = input("") # Variável que recebe o valor do nome (Não precisa colocar nada entre as aspas, devido já ter uma entrada definida)
    matricula = input("") # Variável que recebe o valor da matricula
    print(f"Olá {nome}, Matrícula: {matricula}. Seja bem vindo!") # o f permite que a string contenha variáveis que queremos interpolar. as variáveis devem ir dentro de {}.
    
if __name__ == "__main__":
    main()