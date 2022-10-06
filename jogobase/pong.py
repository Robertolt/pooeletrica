import sys
import pygame
import random

# inicializacao basica
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
FONT_SIZE = 48
VELOCIADADE_DO_RECT_1 = 10
VELOCIADADE_DO_RECT_2 = 10

# criar uma fonte eh necessario para escrever na tela
font = pygame.font.SysFont(None, FONT_SIZE)

# posiçao dos rects
p1_y = 0
p2_y = 0

# posiçao dos rects
bola_vel_abs = 0.5
bola_x = SCREEN_WIDTH//2
bola_y = SCREEN_HEIGHT//2
bola_vy = random.choice([-bola_vel_abs, bola_vel_abs])
bola_vx = random.choice([-bola_vel_abs, bola_vel_abs])

# contadores do placar
contador_1 = 0
contador_2 = 0

# cria uma janela com o tamanho dado
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# enquanto a janela nao for fechada
while True:

    # para cada evento recebido
    for event in pygame.event.get():

        # se for recebido o evento de fechar a janela (ex.: usuario clicou no 'x') ...
        if (event.type == pygame.QUIT) or \
                (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or \
                (pygame.key.get_pressed()[pygame.K_ESCAPE]):
            # ... encerra o programa
            print("Encerrando o programa.")
            sys.exit()

        # faz o rect_1 ir para baixo
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_s) or \
                (pygame.key.get_pressed()[pygame.K_s]):
            if p1_y + 100 <= 600:
                p1_y += 1*VELOCIADADE_DO_RECT_1

        # faz o rect_1 ir para cima
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_w) or \
                (pygame.key.get_pressed()[pygame.K_w]):
            if p1_y >= 0:
                p1_y -= 1*VELOCIADADE_DO_RECT_1

        # faz o rect_2 ir para baixo
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_k) or \
                (pygame.key.get_pressed()[pygame.K_k]):
            if p2_y + 100 <= 600:
                p2_y += 1*VELOCIADADE_DO_RECT_1

        # faz o rect_2 ir para cima
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_i) or \
                (pygame.key.get_pressed()[pygame.K_i]):
            if p2_y >= 0:
                p2_y -= 1*VELOCIADADE_DO_RECT_1

    bola_x = bola_x + bola_vx
    bola_y = bola_y + bola_vy

    if bola_x < 0 or bola_x > SCREEN_WIDTH:
        bola_vx = -bola_vx

    if bola_y < 0 or bola_y > SCREEN_HEIGHT:
        bola_vy = -bola_vy

    # preenche a tela com branco
    screen.fill((255, 255, 255))

    pygame.draw.rect(
        surface=screen,
        color=BLACK,
        rect=(0, p1_y, 25, 100),
        width=0
    )
    pygame.draw.rect(
        surface=screen,
        color=BLACK,
        rect=(SCREEN_WIDTH - 25, p2_y, SCREEN_WIDTH, 100),
        width=0
    )

    pygame.draw.circle(
        surface=screen,
        color=BLACK,
        center=(bola_x, bola_y),
        radius=5,
        width=0
    )

    # cria uma imagem representando o texto
    # os argumentos sao o texto, um valor booleano indicando se
    # deve ser aplicado antialising (use sempre True) e a cor do texto.
    text_img = font.render(f'{contador_1} x {contador_2}', True, (0, 0, 0))

    # desenha a imagem na tela
    screen.blit(text_img, (SCREEN_WIDTH//2 - 40, 40))

    # atualiza a tela
    pygame.display.flip()
