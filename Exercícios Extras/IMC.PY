# Cálculo do IMC

# Nome = Suellen ou o seu nome
# Peso = 50kg ou o seu peso
# Altura = 1.60m ou a sua altura

def main():
    nome = input('Digite seu nome: ')  # input() retorna uma string
    peso = float(input('Digite seu peso: '))    # float() converte a string para um número real
    altura = float(input('Digite sua altura: '))    # float() converte a string para um número real
    # Cálculo do IMC
    imc = peso / (altura ** 2)   # ** é o operador de exponenciação
    print(f'O IMC de {nome} é {imc:.2f}')   # :.2f formata o número com duas casas decimais

if __name__ == '__main__':
    main()
