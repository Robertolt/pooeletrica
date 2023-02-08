n = int(input(''))
contador = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        contador += 1/((i +j) ** 2)
print(f'{contador:.3f}')
