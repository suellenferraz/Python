# Loop while é um laço de repetição que executa um bloco de código enquanto a condição for verdadeira.

# Exemplo de estrutura básica

def main():
    i = 0 # inicializa i com 0
    while i < 5: # enquanto i for menor que 5
        print(i)
        i += 1 # incrementa i em 1
if __name__ == "__main__":
    main()

# Exemplo do while not

def main():
    i = 0 # inicializa i com 0
    while not i == 5: # enquanto i não for igual a 5
        print(i)
        i += 1 # incrementa i em 1
if __name__ == "__main__":
    main()

# While em aninhamento

def main():
    i = 0 # inicializa i com 0
    while i < 5: # enquanto i for menor que 5
        j = 0 # inicializa j com 0
        while j < 5: # enquanto j for menor que 5
            print(f"i: {i}, j: {j}")
            j += 1 # incrementa j em 1
        i += 1 # incrementa i em 1
if __name__ == "__main__":
    main()

# while com if, elif e else

def main():
    i = 0 # inicializa i com 0
    while i < 5: # enquanto i for menor que 5
        if i == 2: # se i for igual a 2
            print("i é igual a 2")
        elif i == 4: # se i for igual a 4
            print("i é igual a 4")
        else: # senão
            print(i)
        i += 1 # incrementa i em
if __name__ == "__main__":
    main()

# for dentro de um while

def main():
    i = 0 # inicializa i com 0
    while i < 5: # enquanto i for menor que 5
        for j in range(5): # para j de 0 a 4
            print(f"i: {i}, j: {j}")
        i += 1 # incrementa i em 1
if __name__ == "__main__":
    main()