"""faça um programa que leia uma linha contendo uma sequencia de números separados por espaço e use funçoes
de strings para exibir o dobro dos números na tela"""


def main():
    linha = input('Digite os numeros desejados em formato de linha: (Ex: 2 120 500 )')
    linha = linha.split(' ')
    for i in range(0, len(linha)):
        print(int(linha[i])*2)


if __name__ == '__main__':
    main()
