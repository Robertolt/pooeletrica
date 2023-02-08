n = int(input(''))
contador = 0
for i in range(1, n+1):
    contador += 1/((2*i) ** 2)
print(f'{contador:.3f}')
