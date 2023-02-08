'''Faça um programa que leia um número inteiro n e então leia n linhas contendo o nome de um estudante e 4 números
indicando as notas em 3 avaliações e o percentual de faltas. Mostre na tela os nomes dos aprovados
 assumindo que o critério de aprovação é ter nota média maior ou igual a 6 e percentual de faltas
 menor ou igual a 25%.
'''

n = int(input())
for i in range(n):
    k = input('').split()
    if ((float(k[1]) + (float(k[2])) + (float(k[3])))/3 >= 6) and (float(k[4]) <= 25):
        print(k[0])

