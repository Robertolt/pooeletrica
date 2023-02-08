"""Suponha que você está desenvolvendo um jogo 2D de tiro ao alvo e você deseja verificar
se um tiro acertou o alvo. Assuma que o tiro e o alvo são círculos e são conhecidas suas
posições e raios."""


alvox = float(input(''))
alvoy = float(input(''))
raio = float(input(''))


tirox = float(input(''))
tiroy = float(input(''))
raio2 = float(input(''))

distancia = ((alvox - tirox)**2 + (alvoy - tiroy)**2)**0.5

if distancia <= (raio + raio2):
    print(True)
else:
    print(False)

