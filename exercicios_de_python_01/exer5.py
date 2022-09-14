"""
Em um campeonato, cada time recebe 3 pontos por vitória, 2 pontos por empate e 1 ponto
por derrota. Faça um programa que leia o número de vitórias, empates e derrotas de um
time e mostre sua pontuação na tela.
"""
v = int(input('insira o numero de vitórias: '))
e = int(input('insira o numero de empates: '))
d = int(input('insira o numero de derrotas: '))

print(f'A pontuação do seu time foi {(v*3)+(e*2)+(d*1)} pontos')
