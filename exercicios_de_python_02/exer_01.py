"""Uma loja vende seus produtos em 5x sem juros para compras até R$ 500,00 e 10x sem
juros para compras acima de R$500,00. O cliente João Gastão sempre faz as compras
no máximo número de prestações possível. Faça um programa que receba o valor de
uma compra do Sr. Gastão e mostre na tela o número de prestações e o valor de cada
uma."""

preco = int(input('Digite o preço da compra: '))
if preco > 500:
    parcelas = preco/10
    print(f'O Sr pagará 10 parcelas de {parcelas}')
else:
    parcelas = preco / 5
    print(f'O Sr pagará 5 parcelas de {parcelas}')
    