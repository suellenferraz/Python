# Exercício 3 do Capítulo 2 das Listas de Linguagem de Programação - ECT3201

def main():
    x = input("").strip().lower() # O strip foi usado remove espaços em branco no início e no final da string. 
    y = input("").strip().lower() # O lower converte todos os caracteres da string para minúsculas. Isso é necessário porque a comparação deve ser insensível a maiúsculas e minúsculas, conforme especificado no enunciado ("ignorando a capitalização").
    
    if x == y: # Usei o if/else para fazer a comparação (==) entre as strings.
        print("São iguais")
    else:
        print("São diferentes")
    
if __name__ == "__main__":
    main()