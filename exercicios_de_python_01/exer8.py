"""
Faça um programa que leia as coordenadas x e y de dois pontos e mostre na tela a distância
entre eles.
"""

x1 = float(input('Digite a coordenada x do primeiro objeto: '))
y1 = float(input('Digite a coordenada y do primeiro objeto: '))
x2 = float(input('Digite a coordenada x do segundo objeto: '))
y2 = float(input('Digite a coordenada y do segundo objeto: '))

distancia = ((x1 - x2)**2 + (y1 - y2)**2)**0.5

print(distancia)
