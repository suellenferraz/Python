def dobrar(numero: float):
    return numero * 2


def triplicar(numero: float):
    return numero * 3


def dividir_por_dois(numero: float):
    return numero / 2


def processar_e_somar_lista(operacao, lista_numeros: list[float]):
    lista_processada = [operacao(num) for num in lista_numeros]
    soma_total = sum(lista_processada)
    return lista_processada, soma_total
  
entrada = list(map(float, input().split()))
print(f"Números originais: {entrada}")

lista_dobrada, soma_dobrada = processar_e_somar_lista(dobrar, entrada)
print("\nOperação: Dobrar")
print(f"Lista processada: {lista_dobrada}")
print(f"Soma dos elementos: {soma_dobrada:.2f}")

lista_triplicada, soma_triplicada = processar_e_somar_lista(triplicar, entrada)
print("\nOperação: Triplicar")
print(f"Lista processada: {lista_triplicada}")
print(f"Soma dos elementos: {soma_triplicada:.2f}")

lista_dividida, soma_dividida = processar_e_somar_lista(dividir_por_dois, entrada)
print("\nOperação: Dividir por dois")
print(f"Lista processada: {lista_dividida}")
print(f"Soma dos elementos: {soma_dividida:.2f}")