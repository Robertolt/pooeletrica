'''

Faça um programa que leia um número inteiro n e então leia n linhas contendo informações sobre produtos separados
por ponto-e-vírgula. Mostre na tela o número de produtos de cada categoria.
Assuma que as categorias podem ser escritas em diferentes casos (minúsculo, maiúsculo, etc.).
'''

n = int(input())

lista = []
dicionario = {}

for i in range(n):
    lista.append(input('').lower().split(';'))

for listas in lista:
    for palavra in listas:
        if palavra in dicionario:
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1


print(f'{lista[0][1]}: {dicionario[lista[0][1]]}')
print(f'{lista[2][1]}: {dicionario[lista[2][1]]}')
