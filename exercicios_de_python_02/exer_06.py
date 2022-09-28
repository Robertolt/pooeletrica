"""Leia 3 números e mostre-os em ordem na tela usando apenas condicionais"""

num1 = int(input('Digite o 1 numero: '))
num2 = int(input('Digite o 2 numero: '))
num3 = int(input('Digite o 3 numero: '))

if (num1 > num2) and (num1 > num3):
    print('Número 1 é o maior')
elif (num2 > num3) and (num2 > num1):
    print('Número 2 é o maior')
elif (num3 > num2) and (num3 > num1):
    print('Número 3 é o maior')
else:
    print('Os números são iguais')
