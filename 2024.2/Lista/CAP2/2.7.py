# Exercício 7 do Capítulo 2 das Listas de Linguagem de Programação - ECT3201
"""Crie um dicionário chamado contato. Peça ao usuário para fornecer os dados para as chaves “nome”, “telefone” e “endereço”. Em seguida, imprima o conteúdo do dicionário."""

def main():
    contato = {} # Dicionário vazio
    
    contato["nome"] = input("") # Coleta o os valores
    contato["telefone"] = input("")
    contato["endereço"] = input("")
    
    nome = contato["nome"] # Acessar os valores coletados
    
    telefone = contato["telefone"]
    
    endereco = contato["endereço"]
    
    print(f"Nome: {nome}, Telefone: {telefone}, Endereço: {endereco}.") # Imprimi os valores associados ao dicionário.
    
    
if __name__ == "__main__":
    main()    
