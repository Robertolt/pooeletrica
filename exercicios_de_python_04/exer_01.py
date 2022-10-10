"""faça uma lista que use comandos de repetição para implementar o slice indexing"""


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista)

indice_inicial = int(input('Digite o índice inicial para fazer a respartição da lista: '))
indice_final = int(input('Digite o índice final para fazer a respartição da lista: '))


print('[', end='')
for i in range(len(lista)):
    while indice_inicial <= i <= indice_final:
        print(lista[i], end=',')
        break

print(']')
