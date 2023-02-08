'''
Faça um programa que leia uma linha contendo uma sequência de números inteiros separados por
espaço e use funções de strings para exibir o dobro dos números na tela.
'''

n = input('').split()
for i in range(len(n)):
    print(int(n[i])*2)