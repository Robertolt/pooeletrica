'''

Faça um programa que leia um número inteiro n e então leia n linhas contendo informações sobre produtos separados
por ponto-e-vírgula. Mostre na tela o número de produtos de cada categoria.
Assuma que as categorias podem ser escritas em diferentes casos (minúsculo, maiúsculo, etc.).
'''

n = int(input())
for i in range(n):
    k = input('').lower().split(';')
    print(k)
    print(k[1])
    contador = 0
    for palavras in range(len(k)):
        if k[1] == k[palavras]:
            contador += 1
    contador = k.count('k[1]')
    print(f'{k[1]}: {contador}')
