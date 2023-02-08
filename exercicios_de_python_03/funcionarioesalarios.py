"""
Escreva uma classe Funcionário que tenha como atributos o nome do
funcionário, o salário-base, o número de atendimentos realizados no
mês, e a titulação (técnico, graduação, mestrado ou doutorado).

Na classe, crie os métodos:

a. __init__: o construtor deve receber os valores dos atributos.

b. __str__: deve retornar uma string no formato “Funcionario(nome,
salario_base=valor, n_atendimentos=valor, titulação=valor)”.



c. salario: deve retornar o salário total do funcionário que é dado
pela soma do salário-base, mais R$25 por atendimento e um bônus por
titulação dado pelo produto do salário de base por um multiplicador
dependente da titulação, sendo 1.0 para técnico, 2.0 para graduação,
5.0 para mestrado e 10 para doutorado.

Faça uma função main que leia uma linha contendo, respectivamente,
 o nome, salário-base, número de atendimentos e titulação de um funcionário,
 use os dados para criar um objeto do tipo Funcionario e mostre na tela uma
 mensagem informando o salário total do funcionário com duas casas decimais.
 Assuma que as titulações serão digitadas sem acento.
"""


class Funcionario:
    def __init__(self, nome, salario_base, n_aten, titulacao):
        self.titulacao = titulacao
        self.n_aten = n_aten
        self.salario_base = salario_base
        self.nome = nome

    def __str__(self):
        return self.nome, self.salario_base, self.n_aten, self.titulacao

    def salario(self):
        if self.titulacao == 'tecnico':
            m = 1
        elif self.titulacao == 'graduacao':
            m = 2
        elif self.titulacao == 'mestrado':
            m = 5
        else:
            m = 10
        return self.salario_base + (self.n_aten * 25) + (self.salario_base * m)


def main():
    lista = []
    comandos = input('').split()
    f = Funcionario



if __name__ == "__main__":
    main()
