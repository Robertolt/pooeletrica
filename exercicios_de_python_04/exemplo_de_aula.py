
def main():
    tempo = input('Digite o tempo de prova: ')  # 1h 25min
    tempo = tempo.strip('min')  # 1h 25
    partes = tempo.split(' ')  # ['1h', '25']
    horas = partes[0].strip('h')  # '1'
    tempohora = int(horas)*3600
    tempomin = int(partes[1])*60
    totaltempo = tempohora + tempomin
    print(totaltempo)


if __name__ == "__main__":
    main()
