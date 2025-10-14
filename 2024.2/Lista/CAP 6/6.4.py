def validar_senha(senha: str) -> list[bool]:
    """
    Valida uma senha com base nos seguintes critérios:
    1. Comprimento mínimo de 8 caracteres.
    2. Contém pelo menos uma letra maiúscula.
    3. Contém pelo menos uma letra minúscula.
    4. Contém pelo menos um número.

    Args:
        senha (str): A senha a ser validada.

    Returns:
        List[bool]: Lista de validações (True ou False) para cada critério.
    """
    # Inicializa a lista de critérios como True
    criterios = [True, True, True, True]

    # Verifica o comprimento mínimo
    if len(senha) < 8:
        criterios[0] = False

    # Contadores para maiúsculas, minúsculas e números
    cont_maiusculas, cont_minusculas, cont_numeros = 0, 0, 0

    for caractere in senha:
        if caractere.isupper():
            cont_maiusculas += 1
        elif caractere.islower():
            cont_minusculas += 1
        elif caractere.isdigit():
            cont_numeros += 1

    # Atualiza os critérios com base nos contadores
    if cont_maiusculas == 0:
        criterios[1] = False
    if cont_minusculas == 0:
        criterios[2] = False
    if cont_numeros == 0:
        criterios[3] = False

    return criterios

def exibir_resultado(criterios: list[bool]) -> None:
    """
    Exibe o resultado da validação de senha.

    Args:
        criterios (List[bool]): Lista de validações (True ou False) para cada critério.
    """
    mensagens = [
        "Comprimento mínimo de 8 caracteres",
        "Pelo menos uma letra maiúscula",
        "Pelo menos uma letra minúscula",
        "Pelo menos um número"
    ]

    for i, criterio in enumerate(criterios):
        print(f"{mensagens[i]}: {'OK' if criterio else 'NÃO'}")

    if all(criterios):
        print("Senha forte!")
    else:
        print("Senha fraca!")

# Entrada do usuário
senha = input().strip()

# Validação e exibição dos resultados
criterios_validados = validar_senha(senha)
exibir_resultado(criterios_validados)
