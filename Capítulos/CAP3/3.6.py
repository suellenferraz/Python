# Exercício 6 do Capítulo 3 das Listas de Linguagem de Programação - ECT3201

def main():
    usuarios_senhas = { #Dicionário com as entradas de autenticação
        "usuario1": "senha123",
        "usuario2": "abc456",
        "usuario3": "123456"
    }
    
    entradas = input().split()  # Lê todas as entradas em uma única linha e divide
    
    usuario_login = entradas[0]  # Primeiro valor é o usuário
    senha_login = entradas[1]    # Segundo valor é a senha
    
    if usuario_login in usuarios_senhas and usuarios_senhas[usuario_login] == senha_login:
        print(f"Login bem-sucedido! Bem-vindo, {usuario_login}")
    else:
        print("Acesso negado. Credenciais inválidas.")

if __name__ == "__main__":
    main()
