"""
Faça um programa que leia as coordenadas x e y de dois pontos e mostre na tela a distância
entre eles.
"""

coordenadasx = (input('').split())
coordenadasy = (input('').split())
x1 = float(coordenadasx[0])
x2 = float(coordenadasx[1])
y1 = float(coordenadasy[0])
y2 = float(coordenadasy[1])

distancia = ((x1 - x2)**2 + (y1 - y2)**2)**0.5

print(distancia)
