"""
Abaixo são listadas algumas sequências de números. Cada número da sequência possui um
índice, sendo o primeiro 0, o segundo 1 e assim por diante. Faça um programa que leia o
índice i de um número e mostre na tela o i-ésimo elemento de cada sequência.
0, 1, 2, 3, 4, 5, 6, ...
4, 5, 6, 7, 8, 9, ...
0, 9, 18, 27, 36, ...
1, -1, 1, -1, 1, -1, ...
2, 3, 5, 9, 17, 33, 65, ...
"""

indice = int(input(''))


# aqui é impressa a primeira lista de números do exercício
indice1 = indice
print(indice1)


# aqui é impressa a segunda lista de números do exercício
indice2 = indice + 4
print(indice2)

# aqui é impressa a terceira lista de números do exercício
indice3 = indice*9
print(indice3)

# aqui é impressa a quarta lista de números do exercício
indice4 = indice

if indice4 % 2 == 0:
    indice4 = 1
else:
    indice4 = -1

print(indice4)

# aqui é impressa a quinta lista de números do exercício
indice5 = indice


if indice5 == 0:
    indice5 = 2
else:
    indice5 = 2 ** indice + 1

print(indice5)


