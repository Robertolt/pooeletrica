"""Faça um programa que solicite que um usuário digite o seu e-mail e idade enquanto os
valores digitados não forem válidos. Assuma que um e-mail é válido se possuir “@” e “.com”
e que a idade é válida se for composta apenas por dígitos numéricos. Use o operador “in” e
o método “isnumeric” para solucionar a questão."""

idade = input('Digite sua idade: ')
email = input('Digite seu e-mail: ')


if idade.isnumeric() and ('@' in email) and email[-4:] == '.com':
    print('E-MAIL válido')
else:
    print('email inválido tente novamente')
