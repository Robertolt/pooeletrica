from abc import ABC, abstractmethod

'''
O objetivo do exercício, é criar um programa para gerenciar uma cartela de investimentos.
Para isto, deverão ser implementadas as classes do diagrama anexado a seguir.

-> #######A classe Portfolio que possui uma lista de investimentos passada como entrada no
construtor e um método rendimento() que deve retornar a soma dos rendimentos da lista de
investimentos. Os tipos de investimentos possíveis são RendaFixa, CompraVenda
(compra e venda de itens), Imóvel e Acoes.

-> #######A classe abstrata Investimento tem como atributos o nome do investimento e o valor
investido. Ela tem como método abstrato rendimento(). Todas as classes que herdam de
Investimento devem implementar este método.

-> A classe RendaFixa herda de Investimento e tem como atributos adicionais a duração
do investimento em meses e a taxa de juros mensais. Sua implementação do método rendimento()
deve retornar os juros totais após a duração do investimento.

->####### A classe CompraVenda também herda de Investimento e tem como atributo adicional o
 valor de venda do bem. Sua implementação do método rendimento() deve retornar a
  diferença entre o preço de venda e o preço de compra.

-> A classe Acoes herda de CompraVenda e tem como atributo adicional o valor total
 de dividendos recebido pelas ações. Ela deve sobrescrever o método rendimento() de
  CompraVenda e somar ao resultado o valor dos dividendos.

-> Por fim, a classe imóvel herda de CompraVenda e tem como atributos adicionais os
 gastos_mensais do imóvel quando este não está alugado, o número de meses que ele
 ficou alugado, o valor do aluguel e a duração do investimento em meses
 (quantos meses se passaram entre a compra e a venda do imóvel). Sua implementação do
 método rendimento() deve além de calcular a diferença entre valor de venda e compra,
 deve subtrair os gastos do imóvel nos meses em que ele não esteve alugado e somar os
 valores dos aluguéis nos demais meses.

A função main do programa é dada a seguir. Envie um arquivo zip contendo a main e o
arquivo investimentos.py.

'''


class Portfolio:
    def __init__(self, RendaFixa, CompraVenda, Imovel, Acoes):
        self.RendaFixa = RendaFixa
        self.CompraVenda = CompraVenda
        self.Imovel = Imovel
        self.Acoes = Acoes

    def rendimento(self):  # deve retornar a soma dos rendimentos
        return sum([self.RendaFixa.rendimento(), self.CompraVenda.rendimento(), self.Imovel.rendimento(),
                    self.Acoes.rendimento()])


class Investimento(ABC):
    def __init__(self, nome, valor_investido):
        self.nome = nome
        self.valor_investido = valor_investido

    @abstractmethod
    def rendimento(self) -> float:
        """ retorna o rendimento """


class RendaFixa(Investimento):
    def __init__(self, nome, valor_investido, taxa, duracao):
        super().__init__(nome, valor_investido)
        self.taxa = taxa
        self.duracao = duracao

    def rendimento(self) -> float:
        return self.valor_investido * (1 * self.taxa) ** self.duracao


class CompraVenda(Investimento):
    def __init__(self, nome, valor_investido, valor_venda):
        super().__init__(nome, valor_investido)
        self.valor_venda = valor_venda

    def rendimento(self) -> float:
        return self.valor_venda - self.valor_investido


class Imovel(CompraVenda):
    def __init__(self, nome, valor_investido, gastos_mensais, meses_alugados, duracao,
                 valor_venda, aluguel, ):
        super().__init__(valor_venda, nome, valor_investido)
        self.duracao = duracao
        self.aluguel = aluguel
        self.meses_alugados = meses_alugados
        self.gastos_mensais = gastos_mensais

    def rendimento(self) -> float:
        return (self.valor_venda - self.valor_investido) + (self.aluguel * self.meses_alugados) - \
               (self.gastos_mensais * (self.duracao - self.meses_alugados))


class Acoes(CompraVenda):
    def __init__(self, nome, valor_venda, valor_investido, dividendos):
        super().__init__(valor_venda, nome, valor_investido)
        self.dividendos = dividendos

    def rendimento(self) -> float:
        return super().rendimento() + self.dividendos


def main():
    portfolio = Portfolio([
        RendaFixa("poupanca", valor_investido=1000, taxa=0.007, duracao=48),
        RendaFixa("LCI-2025", valor_investido=5000, taxa=0.012, duracao=24),
        CompraVenda("Carro", valor_investido=32000, valor_venda=35000),
        Imovel("Casa", valor_investido=150000, valor_venda=170000,
               gastos_mensais=900, meses_alugados=12, aluguel=1600, duracao=24),
        Acoes("Americanas", valor_investido=6000, valor_venda=1000, dividendos=47),
    ])

    rendimento_total = portfolio.rendimento()
    print(f"{rendimento_total:.2f}")


if __name__ == "__main__":
    main()
