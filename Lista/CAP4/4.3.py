# Exercício 3 do Capítulo 4 das Listas de Linguagem de Programação - ECT3201

# Contagem Regressiva: Escreva uma contagem regressiva de 10 a 1, com um intervalo de 1 segundo entre cada número. Para isso, pesquise e utilize o módulo time para pausar a execução do programa por 1 segundo antes de imprimir cada número.
# Lembre-se de importar o módulo time e usar a função time.sleep(1) para criar o atraso desejado. Você pode encontrar mais informações sobre o módulo time
# time = 0.5s


def main():
    import time # Importa a biblioteca time 
    for i in range(10, 0, -1): # Loop que conta de 10 a 1 com um intervalo de 1 segundo entre cada número 
        if i > 1: # Verifica se o número é maior que 1 
            print(i, end=', ') # Imprime o número com uma vírgula no final 
        else: # Caso contrário 
            print(i, end=' ') # Imprime o número sem vírgula no final 
        time.sleep(0.5) # Pausa a execução do programa por 0.5 segundos 
if __name__ == '__main__':
    main()