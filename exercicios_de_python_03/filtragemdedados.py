"""
Faça um programa que leia um número inteiro n e então leia n linhas contendo informações
 sobre produtos separados por ponto-e-vírgula. Use funções de strings para:

a. Remover os valores entre o primeiro e o segundo símbolo de ponto-e-vírgula;
b. Converter o nome do produto para maiúsculo;
c. Substituir “/home/” por “C:/Users/”.

Mostre na tela os resultados das operações.
"""

n = int(input())
for i in range(n):
    k = input('').split(';')
    k.insert(0, k[0].upper())
    k.pop(1)
    k.pop(1)
    lista = k[-1].split('/')
    lista.pop(0)
    lista.pop(0)
    lista.insert(0, ' C:/Users')
    k.pop(-1)
    k.append('/'.join(lista))

    print(';'.join(k))
