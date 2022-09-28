"""Faça um programa que leia a idade da pessoa, a cidade que ela mora, a área que ela
trabalha e um número inteiro indicando se ela possui alguma comorbidade ou não (1
para sim e 0 para não), e mostre na tela se ela tem direito à um dado auxílio. Se pelo
menos um dos critérios abaixo for satisfeito, a pessoa terá direito ao auxílio:
• Morar na Serra e ter mais de 35 anos
• Morar em outra cidade e ter mais de 40 anos
• Trabalhar na área da saúde
• Trabalhar na área da educação
• Ter comorbidades"""

idade = int(input('Digite sua idade: '))
cidade = input('Digite onde você mora: ').lower()
trabalho = input('Digite com que você trabalha: ').lower()
comobidade = int(input('Digite 1 caso tenha alguma comorbidade, caso contrário, 0: '))

if comobidade == 1:
    print('Tem auxílio')
elif (trabalho == 'saude') or (trabalho == 'educaçao'):
    print('Tem auxílio')
elif (cidade == 'serra' and idade > 35) or idade >= 40:
    print('Tem auxílio')
else:
    print('Nao tem auxílio')

