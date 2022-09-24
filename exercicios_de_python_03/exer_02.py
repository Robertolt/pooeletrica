"""Faça um programa que mostre na tela um menu e permita ao usuário escolher uma das
opções 1) Cumprimentar, 2) Notícias e 0) Sair. Se for escolhida a opção 1, o programa deve
exibir a mensagem “Bom dia!” na tela. Se for escolhida a opção 2, o programa deve exibir
“Dia com temperatura agradável e sem perspectiva de chuva”. Se for escolhida a opção 0, o
programa deve ser encerrado. Se qualquer outro valor for digitado, o programa deve exibir
a mensagem “opção inválida”. As operações de exibir o menu e executar a opção escolhida
pelo usuário devem ser repetidas até que seja escolhida a opção 0."""
from time import sleep

print('Bem vindo ao Robô falante, selecione uma ação dele: ')
sleep(2)
print('1) Cumprimentar')
sleep(1)
print('2) Notícias')
sleep(1)
print('0) Sair')
sleep(1)


while True:
    digito = int(input('Insira aqui: '))

    if digito == 1:
        print('Bom dia!')
    elif digito == 2:
        print('Dia com temperatura agradável e sem perspectiva de chuva')
    elif digito == 0:
        print('O programa será encerrado!')
        break
    else:
        print('Por favor, digite um digito válido')
