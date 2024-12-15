import re

def validar_campos(telefone, cpf):
    # Padrão para validar o telefone com dois formatos possíveis
    padrao_telefone = r'^\(\d{2}\) \d{4,5}-\d{4}$'
    
    # Padrão para validar o CPF 
    padrao_cpf = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    

    # Verificar se o telefone é válido
    telefone_valido = re.match(padrao_telefone, telefone) is not None
    
    # Verificar se o CPF é válido (formato correto)
    cpf_valido = re.match(padrao_cpf, cpf) is not None
    
    # Retornar o resultado formatado
    return (f"Telefone válido: {'Sim' if telefone_valido else 'Não'}\n"
            f"CPF válido: {'Sim' if cpf_valido else 'Não'}")

# Testando a função
tel, cpf = input().split(",")
    
# Remover aspas duplas, se presentes
tel = tel.strip('"')
cpf = cpf.strip('"')

print(validar_campos(tel.strip(), cpf.strip()))