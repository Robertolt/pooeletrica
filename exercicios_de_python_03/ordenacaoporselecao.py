'''
Neste exercício você criará uma função para ordenar uma lista de elementos. Não é permitido usar
funções prontas (e.g., sorted ou sort) para resolver esta questão. Devem ser implementadas
as seguintes funções:
1) Uma função que receba uma lista e um número inteiro i e coloque na posição i o menor elemento
encontrado entre as posições i a n, onde n é o tamanho da lista.
2) Uma função que receba a lista e a ordene. A função deve usar a função acima para colocar o
menor elemento na posição 0, o segundo menor na posição 1, o terceiro menor na posição 2 e assim
por diante. Este algoritmo de ordenação é chamado de ordenação por seleção.
'''

lista = input().split()
lista2 = []
for b in range(len(lista)):
    lista2.append(float(lista[b]))


def organizador(n):
    for i in range(len(n)):
        inicio = i
        for k in range(i + 1, len(n)):
            if n[k] < n[inicio]:
                inicio = k
        if n[i] != n[inicio]:
            lista_aux = n[i]
            n[i] = n[inicio]
            n[inicio] = lista_aux

    for elementos in range(len(n)):
        print(f'{float(n[elementos]):.2f}', end=' ')


organizador(lista2)
