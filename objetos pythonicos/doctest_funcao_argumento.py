def executar(f, n):
    for _ in range(n):
        f()


"""
>>> def ola_mundo():
...    print('ola mundo')
...
>>> executar(ola_mundo):
ola mundo
>>> executar(ola_mundo, 2):
ola mundo
ola mundo
"""
