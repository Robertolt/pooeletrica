class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f'{self.dia:02}/{self.mes}/{self.ano}'

    def n_dias(self):
        if self.mes in [4, 6, 9, 11]:
            return 30
        elif self.mes == 2:
            if self.bissexto:
                return 29
            else:
                return 28
        else:
            return 31

    def bissexto(self):
        if self.ano // 400:
            return True
        elif (self.ano // 4 == 0) and (self.ano // 100 != 0):
            return True
        else:
            return False


