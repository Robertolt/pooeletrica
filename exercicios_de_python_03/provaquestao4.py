"""
Faça um programa que leia um número inteiro n e, então, leia n linhas, cada uma
contendo as coordenadas de um vetor (números reais). Calcule a distância euclidiana
 entre os vetores e mostre na tela dois números inteiros representando os índices
 dos vetores mais próximos, com o índice menor primeiro. Em caso de empate, retorne
 o par de índices que foi encontrado primeiro. A distância euclidiana é dada por:

d(x, y) = raiz_quadrada( somatorio_i quadrado(xi - yi) )
"""

n = int(input(''))
pares_ordenated = []

for _ in range(n):
    pares_ordenated.append(input().split())

for i in range(len(pares_ordenated)):
    for p in range(i+1, len(pares_ordenated)):
        x = pares_ordenated[i][0]
        y = pares_ordenated[i][1]