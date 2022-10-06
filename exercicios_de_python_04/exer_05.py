"""Faça um programa que leia um número inteiro n e então leia n linhas contendo o nome
de um estudante e 4 números indicando as notas em 3 avaliações e o percentual de
faltas. Mostre na tela os nomes dos aprovados assumindo que o critério de aprovação
é ter nota média maior ou igual a 6 e percentual de faltas menor ou igual a 25%."""


def main():
    entrada = int(input('Digite a quantidade de linhas: '))
    lista = []
    for _ in range(entrada):
        nome_notas = input('Digite o nome seguido das 3 notas e a frequência em % divididos por um espaço: ')
        nome_notas = nome_notas.split(' ')
        media = (int(nome_notas[1]) + int(nome_notas[2]) + int(nome_notas[3]))/2
        freq = int(nome_notas[4])
        if media >= 6 and freq <= 25:
            lista.append(nome_notas[0])
    print(lista)


if __name__ == '__main__':
    main()
