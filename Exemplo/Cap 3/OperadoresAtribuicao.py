# Exemplos com operadores de atribuição de forma simples.

def main():
    # Atribuição de valores.
    a = 10
    b = 5

    # Exemplos de operadores de atribuição.
    a += b # a = a + b = 10 + 5 = 15
    print(a)

    a -= b # a = a - b = 15 - 5 = 10
    print(a)

    a *= b # a = a * b = 10 * 5 = 50
    print(a)

    a /= b # a = a / b = 50 / 5 = 10
    print(a)

    a %= b # a = a % b = 10 % 5 = 0
    print(a)

    a **= b # a = a ** b = 0 ** 5 = 0
    print(a)

    a //= b # a = a // b = 0 // 5 = 0
    print(a)
if __name__ == "__main__":
    main()

# Exemplo de quando usar com while
# Quando você quer fazer uma operação e atribuir o resultado a mesma variável. 

def main():
    # Atribuição de valores.
    a = 10
    b = 5

    # Exemplos de operadores de atribuição.
    while a > 0: # Enquanto a for maior que 0. Porque o while a>0? Porque a é a variável que está sendo alterada.
        print(a) 
        a -= b # a = a - b = 10 - 5 = 5 
if __name__ == "__main__":
    main()