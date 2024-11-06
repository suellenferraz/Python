# Operadores lógicos são usados para combinar duas ou mais expressões relacionais. Os operadores lógicos em Python são:

# Operador and
# O operador and retorna True se ambas as expressões forem verdadeiras.
# Exemplo:
# Verifica se 5 é maior que 3 e 10 é maior que 5.
print(5 > 3 and 10 > 5)  # True
# Verifica se 5 é maior que 3 e 10 é menor que 5.
print(5 > 3 and 10 < 5)  # False

# Operador or
# O operador or retorna True se pelo menos uma das expressões for verdadeira.
# Exemplo:
# Verifica se 5 é maior que 3 ou 10 é maior que 5.
print(5 > 3 or 10 > 5)  # True
# Verifica se 5 é maior que 3 ou 10 é menor que 5.
print(5 > 3 or 10 < 5)  # True
# Verifica se 5 é menor que 3 ou 10 é menor que 5.
print(5 < 3 or 10 < 5)  # False

# Operador not
# O operador not inverte o valor da expressão.
# Exemplo:
# Verifica se 5 é maior que 3.
print(not 5 > 3)  # False
# Verifica se 5 é menor que 3.
print(not 5 < 3)  # True
# Verifica se 5 é igual a 5.
print(not 5 == 5)  # False
# Verifica se 5 é diferente de 5.
print(not 5 != 5)  # True
# Verifica se 5 é maior que 3 e 10 é menor que 5.
print(not (5 > 3 and 10 < 5))  # True
# Verifica se 5 é maior que 3 ou 10 é menor que 5.
print(not (5 > 3 or 10 < 5))  # False
# Verifica se 5 é maior que 3 e 10 é maior que 5.
print(not (5 > 3 and 10 > 5))  # False
# Verifica se 5 é maior que 3 ou 10 é maior que 5.
print(not (5 > 3 or 10 > 5))  # False

# Operadores lógicos todos juntos
# Exemplo:
# Verifica se 5 é maior que 3 e 10 é maior que 5 ou 10 é menor que 5.
print(5 > 3 and 10 > 5 or 10 < 5)  # True
# Verifica se 5 é maior que 3 e 10 é menor que 5 ou 10 é maior que 5.
print(5 > 3 and 10 < 5 or 10 > 5)  # True

# A sequencia de execução dos operadores lógicos é a seguinte: not, and e or.