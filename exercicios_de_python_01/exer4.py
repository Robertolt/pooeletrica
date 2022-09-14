"""
Suponha que a nota parcial de uma disciplina seja dada pela soma das notas de 2 trabalhos
e 2 provas, sendo que os trabalhos têm peso de 20% cada e as provas têm peso de 30%
cada. Faça um programa que leia as notas dos trabalhos e provas e mostre na tela a média
parcial com duas casas após a vírgula.
"""

trabalho1 = float(input('Nota trabalho 1:'))
trabalho2 = float(input('Nota trabalho 2:'))
prova1 = float(input('Nota prova1:'))
prova2 = float(input('Nota prova2:'))

media_parcial = (trabalho1*0.2 + trabalho2*0.2 + prova1*0.3 + prova2*0.3)
print(f'A sua média parcial foi {media_parcial}')
