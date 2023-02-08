capital_inicial = float(input('Insira o capital inicial: '))
juros_anuais = 1 + float(input('Insira a taxa de juros anual em porcentagem: '))*0.01/12
aporte_mensais = float(input('Insira o aporte mensal inicial: (todo dividendo será reinvestido)'))
tempo_anos = int(input('insira o tempo em anos: '))*12
dividendos_mensais = float(input('insira a porcentagem de dividendos mensais em porcentagem: '))*0.01 + 1

for i in range(tempo_anos):
    capital_inicial *= juros_anuais
    capital_inicial *= dividendos_mensais
    capital_inicial += aporte_mensais
    print(f'O capital no {i+1} mes foi {capital_inicial:.2f}')
