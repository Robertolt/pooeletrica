
import sys
import random
import pygame as pg

SCREEN_WIDTH = 320
SCREEN_HEIGHT = 240
FONT_SIZE = 48

# inicializacao basica
pg.init()

# cria uma janela com o tamanho dado
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# criar uma fonte eh necessario para escrever na tela
font = pg.font.SysFont(None, FONT_SIZE)

# enquanto a janela nao for fechada
while True:

    # para cada evento recebido
    for event in pg.event.get():

        # se for recebido o evento de fechar a janela (ex.: usuario clicou no 'x')
        # ou se a tecla esc for pressionada...
        if (event.type == pg.QUIT) or \
            (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE) or \
                (pg.key.get_pressed()[pg.K_ESCAPE]):
            # ... encerra o programa
            print("Encerrando o programa.")
            sys.exit(0)

    # preenche a tela com branco
    screen.fill((
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    ))

    # Desenha um retangulo vermelho com a configuração especificada
    # e com 2 pixels de largura da borda.
    # IMPORTANTE: nao eh necessario colocar os nomes dos argumentos.
    # Eu so' coloquei para ficar claro o que cada item representa.
    pg.draw.rect(
        surface=screen,
        color=(255, 0, 0),
        # os valores sao (left, top, width, height)
        rect=(50, 30, 20, 50),
        width=2
    )

    # Usando a mesma logica, desenha um circulo preenchido (width=0)
    # da cor azul (0, 0, 255).
    pg.draw.circle(
        surface=screen,
        color=(0, 0, 255),
        center=(200, 200),
        radius=20,
        width=0
    )

    # cria uma imagem representando o texto
    # os argumentos sao o texto, um valor booleano indicando se
    # deve ser aplicado antialising (use sempre True) e a cor do texto.
    text_img = font.render('Exemplo', True, (0, 0, 0))

    # desenha a imagem na tela
    screen.blit(text_img, (120, 40))

    # atualiza a tela
    pg.display.flip()