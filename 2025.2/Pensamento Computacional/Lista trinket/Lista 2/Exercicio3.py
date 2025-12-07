'''
Baseado no problema beecrowd | 1158 (Ultrapassando Soma de Ímpares Consecutivos III)

Imagine que você trabalha como engenheiro de redes em uma empresa de telecomunicações. Sua tarefa é otimizar a distribuição de dados entre várias torres de transmissão para melhorar a cobertura de rede em uma região específica. Para isso, você precisa calcular a capacidade de transmissão de cada torre baseada em certas configurações.

Cada configuração de torre é representada por um par de inteiros X e Y. O inteiro X representa a capacidade inicial de transmissão, e Y indica quantas atualizações consecutivas de capacidade devem ser feitas, onde cada atualização aumenta a capacidade com números ímpares consecutivos. Sua tarefa é calcular a soma das capacidades atualizadas para determinar o aumento total necessário.

Por exemplo, se a capacidade inicial X é 4 e são necessárias 5 atualizações, você deve somar os próximos 5 números ímpares a partir de 4. Se X fosse 7 e fossem necessárias 4 atualizações, você somaria os próximos 4 números ímpares a partir de 7.

Entrada A primeira linha de entrada é um inteiro N que indica a quantidade de casos de teste que vêm a seguir. Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

Saída Imprima a soma dos Y números ímpares consecutivos a partir do valor X.

Exemplo de Entrada 2 4 3 11 2 Exemplo de Saída 21 24
'''

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    primeiro_impar = x if x % 2 != 0 else x + 1
    soma = sum(primeiro_impar + 2 * i for i in range(y))
    
    print(soma)