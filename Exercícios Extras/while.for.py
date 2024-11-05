# Exercício para diferenciar o uso de while e for

# Escreva um programa que leia um número inteiro positivo n e imprima todos os números de 1 a n ao lado de seus quadrados, conforme o exemplo abaixo:
def main():
    n = int(input("Digite um número inteiro positivo: "))
    for i in range(1, n + 1):
        print(f"{i} {i ** 2}")
if __name__ == "__main__":
    main()

# Exercício para while: Escreva um programa que leia um número inteiro positivo n e imprima todos os números de 1 a n ao lado de seus quadrados, conforme o exemplo abaixo:
def main():
    n = int(input("Digite um número inteiro positivo: "))
    i = 1
    while i <= n:
        print(f"{i} {i ** 2}")
if __name__ == "__main__":
    main()

# A diferença do while e do for é que o for é mais simples e direto, enquanto o while é mais flexível e pode ser mais complexo. Suas traduções é que o for é mais utilizado para repetições com um número fixo de vezes, enquanto o while é mais utilizado para repetições com um número variável de vezes.
# for é traduzido como "para", enquanto while é traduzido como "enquanto".