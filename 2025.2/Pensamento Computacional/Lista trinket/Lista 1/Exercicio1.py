'''
Faça um programa usando Phyton que leia o valor de uma compra e a opção de pagamento (V – para pagamento à vista ou P – para pagamento parcelado). Caso o cliente pague à vista, terá um desconto de 5%, caso pague em 3 vezes terá um acréscimo de 8%. O programa deve mostrar o valor da compra e o valor à vista ou valor a prazo (valor total e o valor de cada parcela).

Entrada Qual o valor da compra?

Saída 500

Como gostaria de pagar: à vista (V) ou à prazo (P)? V Valor à pagar: 475 Qual o valor da compra? 500

Como gostaria de pagar: à vista (V) ou à prazo (P)? P

Valor à pagar: 540

Parcela 1: 180

Parcela 2: 180

Parcela 3: 180
'''


valor = float(input("Qual o valor da compra? "))
opcao = input("Como gostaria de pagar: à vista (V) ou à prazo (P)? ").upper()

if opcao == 'V':
    final = valor - (valor * 0.05) 
    print(f"Valor à pagar: {final:.0f}")

elif opcao == 'P':
    total_prazo = valor + (valor * 0.08)
    parcela = total_prazo / 3
    
    print(f"Valor à pagar: {total_prazo:.0f}")
    print(f"Parcela 1: {parcela:.0f}")
    print(f"Parcela 2: {parcela:.0f}")
    print(f"Parcela 3: {parcela:.0f}")