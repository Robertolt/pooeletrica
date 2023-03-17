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
print(pares_ordenated)
for coord in range(len(pares_ordenated)):
    x = float(pares_ordenated[coord][0])
    y = float(pares_ordenated[coord][1])
    for i in range(len(pares_ordenated)):
        xi = float(pares_ordenated[i][0])
        yi = float(pares_ordenated[i][1])
        if (x - xi) and (y - yi) == 0:
            pass
        else:
            pass


