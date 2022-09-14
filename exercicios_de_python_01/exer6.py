"""
Você possui um capital inicial C para fazer um investimento
e identificou duas possibilidades:
• Investimento 1: rende 10% de C to do mes
• Investimento 2: utiliza juros compostos e rende 1% do
montante acumulado ao mês. Isto é, se C = 100, no
primeiro mês o retorno será 1% de C que é 1. O
acumulado passará a ser 101. No mês 2, o rendimento
será 1% de 101 que é 1,1 e o acumulado passará a ser
102,1.
Faça um programa que mostre na tela a soma dos
rendimentos após T meses. A partir de que mês o
investimento 2 passa a ser mais vantajoso que o 1?
"""
capital = float(input('Digite o capital: '))
capital_simples = capital
mensal_simples = capital_simples*0.1
capital_composto = capital
tempo = 0

while capital_simples >= capital_composto:
    capital_simples += mensal_simples
    capital_composto += capital_composto*0.01
    tempo += 1
    print(capital_simples)
    print(capital_composto)
    print(tempo)

print(f'O investimento 2 passa a ser mais vantajoso em {tempo} meses')
