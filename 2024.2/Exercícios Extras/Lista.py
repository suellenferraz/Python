# Uma lista com nome de frutas, no qual vamos verificar se as frutas percentem ou não a lista e também vamos remover e adicionar.

# Lista de frutas
# frutas = ["banana", "maçã", "uva", "laranja", "manga", "abacaxi", "goiaba", "melancia", "melão", "morango"]

def main():
    frutas = ["banana", "maçã", "uva", "laranja", "manga", "abacaxi", "goiaba", "melancia", "melão", "morango"]
    # Recebendo a fruta
    fruta = input("Digite o nome da fruta: ")
    # Verificando se a fruta está na lista
    if fruta in frutas:
        print(f"{fruta} está na lista.")
        # Removendo a fruta da lista
        frutas.remove(fruta)
        print(f"{fruta} foi removida da lista.")
    else:
        print(f"{fruta} não está na lista.")
        # Adicionando a fruta na lista
        frutas.append(fruta)
        print(f"{fruta} foi adicionada na lista.")
    print(frutas)
if __name__ == "__main__":
    main()