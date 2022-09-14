"""
Abaixo são listadas algumas sequências de números. Cada número da sequência possui um
índice, sendo o primeiro 0, o segundo 1 e assim por diante. Faça um programa que leia o
índice i de um número e mostre na tela o i-ésimo elemento de cada sequência.
0, 1, 2, 3, 4, 5, 6, ...
4, 5, 6, 7, 8, 9, ...
0, 9, 18, 27, 36, ...
1, -1, 1, -1, 1, -1, ...
2, 3, 5, 9, 17, 33, 65, ...
2, -1, 8, -4, 26, -16, 98, ...
"""

indice = int(input('Digite a posição: '))
termo = int(input('Digite a i-ésima posição da sequencia: '))

# aqui é impressa a primeira lista de números do exercício
indice1 = indice
termo1 = termo
print(indice1)
print(termo1)

# aqui é impressa a segunda lista de números do exercício
indice2 = indice + 4
termo2 = termo + 4
print(indice2)
print(termo2)

# aqui é impressa a terceira lista de números do exercício
indice3 = indice*9
termo3 = termo*9
print(indice3)
print(termo3)

# aqui é impressa a quarta lista de números do exercício
indice4 = indice
termo4 = termo

if indice4 % 2 == 0:
    indice4 = 1
else:
    indice4 = -1

if termo4 % 2 == 0:
    termo4 = 1
else:
    termo4 = -1

print(indice4)
print(termo4)

# aqui é impressa a quinta lista de números do exercício
indice5 = indice
termo5 = termo

if indice5 == 0:
    indice5 = 2
else:
    indice5 = 2 ** indice + 1

if termo5 == 0:
    termo5 = 2
else:
    termo5 = 2 ** termo + 1

print(indice5)
print(termo5)

# aqui é impressa a sexta lista de números do exercício
indice6 = indice
termo6 = termo

print(indice2)
print(termo2)
