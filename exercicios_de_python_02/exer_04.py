"""Em uma disciplina prática, o aluno é aprovado se desenvolver um sistema ou se tirar
mais de 60 pontos em uma prova e ter 75% de presença. Entrada: um número
indicando se o sistema foi desenvolvido (1 se sim e 0 se não), a nota da prova e a
frequência. Saída: Uma mensagem dizendo se o aluno foi aprovado ou não."""

nota = int(input('Digite a nota (0 a 100): '))
freq = int(input('Digite a frequência (%): '))
sist = int(input('Digite 1 se fez o sistema, ou 0 se não fez: '))

if ((nota >= 60) or (sist == 1)) and (freq >= 75):
    print('Parabéns, foi aprovado')
else:
    print('Reprovou')
