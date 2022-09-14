"""
Suponha que um trabalho pague 5% do salário de seus funcionários como contribuição do
INSS e uma previdência privada de 2%. Faça um programa que leia o nome e o salário de
uma pessoa, e mostre na tela os valores das contribuições e o salário líquido após os
descontos com 2 casas após a vírgula. Exemplo:
Digite seu nome: Luiz
Digite seu salário: 2000
Ola luiz, seguem as informações:
Contribuição de INSS: 100.00 reais
Contribuição de previdência privada: 40.00 reais
Salário líquido: 1860.00 reais
"""

nome = input('Digite seu nome: ')
salario = int(input('Digite seu salário: '))
print(f'Ola {nome}, seguem as informações: ')
inss = salario*0.05
pp = salario*0.02
print(f'Contribuição de INSS: {inss:.2f} reais')
print(f'Contribuição de previdência privada: {pp:.2f} reais')
salario_liquido = salario - (inss + pp)
print(f'Salário líquido: {salario_liquido:.2f} reais')
