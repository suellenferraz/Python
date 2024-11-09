# Exemplos de como utilizar exit() e break em um loop while/for.

# Exit() em um loop for

def main():
    for i in range(5): # Vai de 0 a 4
        if i == 2:  # Quando i for igual a 2, ele vai sair do loop
            exit() # Vai sair do loop
        print(i) 
if __name__ == "__main__":
    main()
    
# Exit() em um loop while

def main():
    i = 0
    while i < 5: # Enquanto i for menor que 5
        if i == 2: # Quando i for igual a 2, ele vai sair do loop
            exit() # Vai sair do loop, no caso usa o exit, porque ele vai sair do programa.
        print(i) 
        i += 1 # Porque incrementar o i?, para que ele não fique em um loop infinito, dessa forma sempre colocamos um incremento.
if __name__ == "__main__":
    main()

# Break em um loop for

def main():
    for i in range(5): # Vai de 0 a 4 
        if i == 2:  # Quando i for igual a 2, ele vai sair do loop
            break # Vai sair do loop, no caso usa o break, porque ele vai sair do loop e continuar o programa.
        print(i) 
if __name__ == "__main__":
    main()

# Break em um loop while

def main():
    i = 0
    while i < 5: # Enquanto i for menor que 5
        if i == 2: # Quando i for igual a 2, ele vai sair do loop
            break # Vai sair do loop
        print(i)
        i += 1 # Vai incrementar o i
if __name__ == "__main__":
    main()