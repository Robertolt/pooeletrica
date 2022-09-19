"""
Considere um jogo que tenha um tanque com
um canhão que se move ao em relação ao eixo
vertical. Faça um programa que leia a posição
do tanque (ty, tx) e seu tamanho (h, w), além
do ângulo do canhão 𝜃 e seu tamanho t.
Mostre na tela a posição da base do canhão
(by, bx) assumindo que ela está na metade da
largura do tanque e a posição da ponta do
canhão (cy,cx).

"""
import math

tx = float(input('Insira a coordenada tx: '))
ty = float(input('Insira a coordenada ty: '))
w = float(input('Insira o tamanho horizontal do tanque: '))
t = float(input('Insira o tamanho do canhão do tanque: '))
theta = float(input('Insira o angulo do canhão: '))

# pelo enunciado, sabe-se que bx = tx + w/2 onde w é o tamanho horizontal do tanque e tbm que by = ty, logo:
by = ty
bx = tx + w/2

# para encontrar a ponta do canhão cx = bx + oposto e cy = by + adjacente
oposto = math.sin(math.radians(theta))*t
adjacente = math.cos(math.radians(theta))*t
cx = bx + oposto
cy = by + adjacente

print(f'A base do canhão está nas coordenadas ({bx},{by}) e a ponta do canhão está nas coordenadas ({cx},{cy})')
