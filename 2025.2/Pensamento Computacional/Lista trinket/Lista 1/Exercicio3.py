'''
Imagine que você está planejando uma viagem para o Vale do Silício no final de setembro. Você quer saber como as temperaturas locais podem variar em diferentes escalas de temperatura para se preparar adequadamente. A previsão do tempo local indica a temperatura em graus Fahrenheit, mas você também gostaria de saber como essa temperatura seria em Celsius, já que é a sua habitual. Como também é curioso com relação à diferentes escalas, por que não saber como ficaria o valor em Kelvin?

Ao pensar sobre o assunto, você pensou que seu problema deve ser o mesmo passado por várias outras pessoas e decidiu que vai ajudar. Para isso, você precisa escrever um programa em Phyton que permita ao usuário informar a temperatura (em números reais) e a escala utilizada (Celsius, Fahrenheit ou Kelvin). A saída do programa será a temperatura nas três escalas, com duas casas decimais de precisão. A entrada é composta pelo valor da temperatura, seguida de uma letra que vai indicar a escala em que ela está.

Obs: veja que não é necessário imprimir uma mensagem solicitando que o usuário digite a temperatura. Basta fornecer os dados solicitados no mesmo formato que os exemplos a seguir.

Entrada 68 F

Saída Temperatura em Celsius: 20.00 °C Temperatura em Fahrenheit: 68.00 °F Temperatura em Kelvin: 293.15 K

Entrada: 300 K

Saida: Temperatura em Celsius: 26.85 °C Temperatura em Fahrenheit: 80.33 °F Temperatura em Kelvin: 300.00 K

Entrada 25 C

Saida: Temperatura em Celsius: 25.00 °C Temperatura em Fahrenheit: 77.00 °F Temperatura em Kelvin: 298.15 K
'''

temp_input = input().split()
temp_value = float(temp_input[0])
temp_scale = temp_input[1].upper()

if temp_scale == 'C':
    celsius = temp_value
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
elif temp_scale == 'F':
    fahrenheit = temp_value
    celsius = (fahrenheit - 32) * 5/9
    kelvin = celsius + 273.15
elif temp_scale == 'K':
    kelvin = temp_value
    celsius = kelvin - 273.15
    fahrenheit = (celsius * 9/5) + 32
print(f"Temperatura em Celsius: {celsius:.2f} °C")
print(f"Temperatura em Fahrenheit: {fahrenheit:.2f} °F")
print(f"Temperatura em Kelvin: {kelvin:.2f} K")