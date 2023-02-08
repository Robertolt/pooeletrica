"""Escreva programas que leiam um número inteiro n e mostrem na tela os n primeiros
números das sequências abaixo. Faça versões dos programas usando for e while.
0, 1, 2, 3, 4, 5
5, 4, 3, 2, 1, 0
7, 9, 11, 13, 15, 17, 19
21, 18, 15, 12, 9"""

digito = int(input(''))

# primeira sequência


pa = 0 + (digito - 1)
for i in range(0, pa):
    print(i, end=', ')
print(pa)

# segunda sequencia
pa = 5 + (digito - 1)*(-1)
for i in range(5, pa, -1):
    print(i, end=', ')
print(pa)

# terceira seq

pa = 7 + (digito - 1)*2
for i in range(7, pa, 2):
    print(i, end=', ')
print(pa)

# quarta

pa = 21 + (digito - 1)*(-3)
for i in range(21, pa, -3):
    print(i, end=', ')
print(pa)



