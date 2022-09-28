import sys
import pygame

SCREEN_WIDTH = 320
SCREEN_HEIGHT = 240

# inicializacao basica
pygame.init()

# cria uma janela com o tamanho dado
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# enquanto a janela nao for fechada
while True:

    # para cada evento recebido
    for event in pygame.event.get():

        # se for recebido o evento de fechar a janela (ex.: usuario clicou no 'x') ...
        if event.type == pygame.QUIT:
            # ... encerra o programa
            print("Encerrando o programa.")
            sys.exit()

    # preenche a tela com branco
    screen.fill((255, 255, 255))

    # atualiza a tela
    pygame.display.flip()
