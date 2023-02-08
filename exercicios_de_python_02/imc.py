"""
Faça um programa que leia a altura (em metros) o peso (em Kg) de uma pessoa,
calcule seu IMC e mostre na tela em qual categoria ela se encontra.
O IMC é dado pela divisão do peso pela altura ao quadrado. As categorias são:

IMC (kg/m2) Categoria
até 24,99 Normal
25 - 29,99 Pré-obeso
30 - 34,99 Obesidade classe I
>= 35 Obesidade classe II
"""

altura = float(input(''))
peso = float(input(''))
imc = peso / (altura ** 2)

if imc >= 35:
    print('Obesidade classe II')
elif imc >= 30:
    print('Obesidade classe I')
elif imc >= 25:
    print('Pré-obeso')
else:
    print('Normal')
