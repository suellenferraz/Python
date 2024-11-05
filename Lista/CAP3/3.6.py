# Exercício 6 do Capítulo 3 das Listas de Linguagem de Programação - ECT3201
"""Desenvolva um sistema de autenticação que utilize um dicionário chamado usuarios_senhas para armazenar os nomes e as senhas de dois usuários. O programa deve solicitar que o usuário insira seu nome de usuário e senha. Em seguida, o sistema deve verificar se as credenciais inseridas correspondem às armazenadas no dicionário. Se as credenciais estiverem corretas, o programa deve exibir uma mensagem de “Login bem-sucedido! Bem-vindo, usuário.”. Caso contrário, deve informar ao usuário “Acesso negado. Credenciais inválidas.”.
Obs: Serão armazenados apenas três usuários."""

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
