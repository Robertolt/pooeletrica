"""
Em quadrilátero é um quadrado se seus lados forem iguais e o ângulo entre seus lados
for de 90°. Faça um programa que leia 4 números representando os tamanhos dos
lados do quadrilátero e mais 4 números representando os ângulos entre os lados e
mostre na tela uma mensagem informando se o quadrilátero é um quadrado
"""

lado1 = int(input('Digite o tamanho do lado1: '))
lado2 = int(input('Digite o tamanho do lado2: '))
lado3 = int(input('Digite o tamanho do lado3: '))
lado4 = int(input('Digite o tamanho do lado4: '))

angulo1 = float(input('Digite o angulo 1: '))
angulo2 = float(input('Digite o angulo 2: '))
angulo3 = float(input('Digite o angulo 3: '))
angulo4 = float(input('Digite o angulo 4: '))

if (lado1 == lado2) and (lado1 == lado3) and (lado1 == lado4):
    if (angulo1 == 90) and (angulo1 == angulo2) and (angulo1 == angulo3) and (angulo1 == angulo4):
        print('É um quadrado')
else:
    print('Não é um quadrado')