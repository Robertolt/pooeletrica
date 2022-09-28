"""Escreva programas que leiam um número inteiro n e mostrem na tela os n primeiros
números das sequências abaixo. Faça versões dos programas usando for e while.
0, 1, 2, 3, 4, 5
5, 4, 3, 2, 1, 0
7, 9, 11, 13, 15, 17, 19
21, 18, 15, 12, 9
3, 4, 6, 7, 9, 10, 12, 13, 15, 16"""

digito = int(input('Digite até onde devo te mostrar a sequência: '))

# primeira sequência


for i in range(digito):
    print(i, end=', ')

print(digito)

# segunda sequencia

for i in range(digito, 0, -1):
    print(i, end=', ')

print(0)

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

# quinta sequ

