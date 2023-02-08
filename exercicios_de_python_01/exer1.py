"""
Suponha que uma bola seja lançada a partir da posição 0 em uma roleta com tamanho n.
Suponha ainda que você saiba que ela vai passar por k casas. Faça um programa leia os
valores de n e k e mostre na tela o número de voltas completas a bola irá dar na roleta e em
qual casa ela irá terminar.
Na figura ao lado, a roleta tem tamanho n = 11 (veja
que ela inicia da posição 0). Se a bola visitar k = 25
casas, ela irá realizar 2 voltas completas e terminará
na posição 3.
"""
numeros = input('')
n = int(numeros.split()[0])
k = int(numeros.split()[1])


voltas = k // n
casas = k % n

print(voltas, casas)
