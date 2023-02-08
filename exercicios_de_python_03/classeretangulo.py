'''
Crie uma classe Circulo que tenha como atributo o raio e uma classe Retangulo que tenha como
atributos a altura
e largura. Em ambas as classes, crie um construtor que receba o valor dos atributos e métodos
área e perímetro.

Escreva uma função main que leia um número inteiro n e, em seguida, leia os dados de n formas
(formas são retângulos ou círculos). A primeira letra da linha indica se os dados são de um
circulo (C) ou retângulo (R). Para cada linha, crie um objeto do tipo definido pela letra e
adicione o objeto em uma lista.

Ao final, mostre na tela a soma das áreas e dos perímetros das formas, nesta ordem, com 1
casa depois da vírgula. A área e perímetro de cada forma deve ser calculada usando os
métodos da classe. Na questão, assuma PI=3.1415.

IMPORTANTE: Existem formas mais simples de resolver a questão, mas as operações devem ser
 feitas como especificado. O objetivo da questão é avaliar a capacidade do aluno de criar
  classes e objetos, e de manipular listas de objetos.'''


class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.1415 * (self.raio ** 2)

    def perimetro(self):
        return 2 * 3.1415 * self.raio


class Retangulo:
    def __init__(self, altura, largura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return (self.largura * 2) + (self.altura * 2)


def main():
    lista = []
    n = int(input(''))
    for i in range(n):
        comandos = input('').split()
        if comandos[0] == 'C':
            c = Circulo(float(comandos[1]))
            lista_circulo = [c, c.area(), c.perimetro()]
            lista.append(lista_circulo)
        else:
            r = Retangulo(float(comandos[1]), float(comandos[2]))
            lista_retangulo = [r, r.area(), r.perimetro()]
            lista.append(lista_retangulo)
    areas = 0
    perimetros = 0
    for k in range(len(lista)):
        areas += float(lista[k][1])
        perimetros += float(lista[k][2])

    print(f'{areas:.1f} {perimetros:.1f}')


if __name__ == "__main__":
    main()
