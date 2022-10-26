
class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia  # d1.dia = 29
        self.mes = mes  # d1.mes = 02
        self.ano = ano  # d1.ano = 2001 print d1.dia

    def __str__(self):
        return f'{self.dia}/{self.mes:02}/{self.ano:04}'  # sempre retorna uma f'

    def bissexto(self):
        if self.ano % 400 == 0:
            return True
        elif (self.ano % 4 == 0) and (self.ano % 100 != 0):
            return True
        else:
            return False

    def n_dias(self):
        if self.mes in (4, 6, 9, 11):
            return 30
        elif self.mes == 2:
            if self.bissexto():
                return 29
            else:
                return 28
        else:
            return 31

    def valida(self):
        if (self.mes < 1) and (self.mes <= 12):
            return False
        if self.ano < 0:
            return False
        if (self.dia < 1) or (self.dia > self.n_dias()):
            return False
        return True

    def diferenca(self, d2):
        contador_dias_d1 = 0
        contador_dias_d2 = 0

        contador_dias_d1 += self.dia
        contador_dias_d2 += d2.dia

        for i in range(1, self.mes):
            self.mes = i
            contador_dias_d1 += self.n_dias()
            print(self.n_dias())

        for i in range(1, d2.mes):
            d2.mes = i
            contador_dias_d2 += d2.n_dias()
            print(d2.n_dias())

        resultado = contador_dias_d1 - contador_dias_d2

        return resultado


def main():
    dados_d1 = input().split()
    dados_d2 = input().split()
    d1_dia = int(dados_d1[0])
    d1_mes = int(dados_d1[1])
    d1_ano = int(dados_d1[2])
    d2_dia = int(dados_d2[0])
    d2_mes = int(dados_d2[1])
    d2_ano = int(dados_d2[2])

    d1 = Data(d1_dia, d1_mes, d1_ano)
    d2 = Data(d2_dia, d2_mes, d2_ano)

    datas_validas = True

    if d1.valida():  # Data.valida(self=d1)
        print(d1, 'e valida')
    else:
        print(d1, 'e invalida')
        datas_validas = False

    if d2.valida():  # Data.valida(self=d2)
        print(d2, 'e valida')
    else:
        print(d2, 'e invalida')
        datas_validas = False

    if datas_validas:
        print('A diferença eh de', d1.diferenca(d2))

    d = Data(1, 1, 2000)

    if d.bissexto():
        print('Ano é bissexto')
    else:
        print('Ano n é bissexto')


if __name__ == '__main__':
    main()
