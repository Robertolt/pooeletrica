from cmath import inf

lista = input('').split()
minimo = inf
maximo = -inf
ordem_minimo = 0
ordem_maximo = 0

for i in range(len(lista)):
    if float(lista[i]) <= minimo:
        minimo = float(lista[i])
        ordem_minimo = i
    elif float(lista[i]) >= maximo:
        maximo = float(lista[i])
        ordem_maximo = i


print(ordem_minimo, ordem_maximo)
