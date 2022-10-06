"""use comandos de repetiçao para implementar funçoes para buscar o minimo,
máximo, soma e média de uma lista ou tupla"""

lista = [150, -2002, -3, 4000, 554841, 6568491563]
soma = 0
maximo = 0
minimo = 0

for i in lista:
    print(i)
    maximo = max(maximo, i)
    minimo = min(minimo, i)
    soma += i

media = soma/len(lista)
print(f'O número máximo é {maximo}, o mínimo é {minimo}, a soma é {soma} e a média é {media}')
