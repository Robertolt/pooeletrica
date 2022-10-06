"""use comandos de repetição para implementar funções para buscar o índice
 do maior elemento e o índice do menor elemento de uma lista"""

lista = [0, -1, 4, 10, 8]

maximo = 0
minimo = 0
i_max = 0
i_min = 0


for i in range(len(lista)):
    if lista[i] > lista[i_max]:
        i_max = i
    if lista[i] < lista[i_min]:
        i_min = i

print(f'O índice máximo é {i_max} que é {lista[i_max]} e '
      f'o índice mínimo é {i_min} que é {lista[i_min]}')
