# Exemplos de como utilizar exit() e break em um loop while/for.

# Exit() em um loop for

def main():
    for i in range(5):
        if i == 2:
            exit()
        print(i)
if __name__ == "__main__":
    main()
    
# Exit() em um loop while

def main():
    i = 0
    while i < 5:
        if i == 2:
            exit()
        print(i)
        i += 1
if __name__ == "__main__":
    main()

# Break em um loop for

def main():
    for i in range(5):
        if i == 2:
            break
        print(i)
if __name__ == "__main__":
    main()

# Break em um loop while

def main():
    i = 0
    while i < 5:
        if i == 2:
            break
        print(i)
        i += 1
if __name__ == "__main__":
    main()