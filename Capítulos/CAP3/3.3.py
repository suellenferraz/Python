# Exercício 3 do Capítulo 3 das Listas de Linguagem de Programação - ECT3201

def main():
    C = float(input("")) # Entrada em ponto flutuante (float) do Celsius
    fahrenheit = (9/5)*C+32 # Fórmula de conversão de Celsius para Fahrenheit
    
    print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}") # Saída com 2 casas decimais (:.2f)

if __name__ == "__main__":
    main()