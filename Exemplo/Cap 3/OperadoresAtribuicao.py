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