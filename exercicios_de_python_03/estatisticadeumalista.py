'''
Faça um programa que leia um número n e então leia uma sequência de números e salve-os em uma lista.
Por fim, mostre na tela o mínimo, máximo e a soma da lista.
'''

n = int(input())
lista = []
for i in range(n):
    k = float(input(''))
    lista.append(k)

lista.sort()
print(f'{lista[0]:.2f} {lista[-1]:.2f} {sum(lista):.2f}')

