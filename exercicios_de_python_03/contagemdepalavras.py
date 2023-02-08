lista = []
dicionario = {}

lista.append(sorted(input('').lower().split()))

for listas in lista:
    for palavra in listas:
        if palavra in dicionario:
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1

for k, v in dicionario.items():
    print(k, v)

