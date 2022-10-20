import sys
import random
import pygame


class ConfigJogo:
    LARGURA_TELA = 640
    ALTURA_TELA = 480
    COR_BARRA = (0, 0, 0)
    COR_BOLA = (0, 0, 0)
    VELOCIDADE_BARRA = 0.2
    VELOCIDADE_BOLA = random.choice([-VELOCIDADE_BARRA, VELOCIDADE_BARRA])
    LARGURA_BARRA = (0.01 * LARGURA_TELA)
    ALTURA_BARRA = (0.1 * LARGURA_TELA)
    POS_INICIAL_BARRA_ESQUERDA = (0.1 * LARGURA_TELA)
    POS_INICIAL_BARRA_DIREITA = (0.9 * LARGURA_TELA - LARGURA_BARRA)
    POS_INICIAL_BOLA = (LARGURA_TELA // 2, ALTURA_TELA // 2)
    TAMANHO_FONTE = 48


class Barra:

    def __init__(self, posicao):
        self.posicao = posicao
        self.velocidade = 0

    def mover_pra_cima(self):
        self.velocidade = -ConfigJogo.VELOCIDADE_BARRA

    def mover_pra_baixo(self):
        self.velocidade = ConfigJogo.VELOCIDADE_BARRA

    def parar(self):
        self.velocidade = 0

    def atualizar_posicao(self):
        x, y = self.posicao  # (valor_x, valor_y)
        novo_y = y + self.velocidade

        if (0 <= novo_y) and (novo_y + ConfigJogo.ALTURA_BARRA < ConfigJogo.ALTURA_TELA):
            self.posicao = (x, novo_y)

    def desenha(self, tela):
        x = self.posicao[0]
        y = self.posicao[1]
        l = ConfigJogo.LARGURA_BARRA
        a = ConfigJogo.ALTURA_BARRA
        pygame.draw.rect(
            surface=tela,
            color=ConfigJogo.COR_BARRA,
            rect=(x, y, l, a),
            width=0
        )


class Bola:

    def __init__(self, posicao):
        self.posicao = posicao
        self.velocidade_x = 0
        self.velocidade_y = 0

    def parar(self):
        self.velocidade_x = 0
        self.velocidade_y = 0

    def mover_em_x(self):
        self.velocidade_x = ConfigJogo.VELOCIDADE_BOLA

    def mover_em_y(self):
        self.velocidade_y = ConfigJogo.VELOCIDADE_BOLA

    def atualizar_posicao_x(self):
        x, y = self.posicao
        novo_x = x + self.velocidade_x
        self.posicao = (novo_x, y)
        if (0 >= novo_x) or (novo_x >= ConfigJogo.LARGURA_TELA):
            self.velocidade_x = - self.velocidade_x

    def atualizar_posicao_y(self):
        x, y = self.posicao
        novo_y = y + self.velocidade_y
        self.posicao = (x, novo_y)
        if (0 >= novo_y) or (novo_y >= ConfigJogo.ALTURA_TELA):
            self.velocidade_y = -self.velocidade_y

    def colisao_esqueda(self):
        x, y = self.posicao
        posicao_x, posicao_y = Bola.__init__(self, posicao=self.posicao).posicao
        if (x == posicao_x) and ((y >= posicao_y) and
                                 (y <= posicao_y + ConfigJogo.ALTURA_BARRA)):
            self.velocidade_x = -self.velocidade_x

    def desenha(self, tela):
        x = self.posicao[0]
        y = self.posicao[1]
        pygame.draw.circle(
            surface=tela,
            color=ConfigJogo.COR_BOLA,
            center=(x, y),
            radius=5,
            width=0
        )


class EstadoJogo:
    # placar
    def placar(self, tela):
        font = pygame.font.SysFont(None, ConfigJogo.TAMANHO_FONTE)
        text_img = font.render(f'{contador_1} x {contador_2}', True, (0, 0, 0))
        tela.blit(text_img, (ConfigJogo.LARGURA_TELA // 2 - 40, 40))

    # tempo de partida
    pass


class Jogo:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((ConfigJogo.LARGURA_TELA,
                                             ConfigJogo.ALTURA_TELA))
        py = ConfigJogo.ALTURA_TELA // 2 - ConfigJogo.ALTURA_BARRA // 2
        px = ConfigJogo.POS_INICIAL_BARRA_ESQUERDA
        self.barra_esquerda = Barra(posicao=(px, py))

        px = ConfigJogo.POS_INICIAL_BARRA_DIREITA
        self.barra_direita = Barra(posicao=(px, py))

        # self.barra_direita.mover_pra_cima()
        # self.barra_esquerda.mover_pra_baixo()

        # Configurações da bola
        self.bola = Bola(posicao=ConfigJogo.POS_INICIAL_BOLA)

    def rodar(self):
        self.bola.mover_em_x()
        self.bola.mover_em_y()
        while True:
            self.tratamento_eventos()
            self.atualiza_estado()
            self.desenha()

    def tratamento_eventos(self):
        pygame.event.get()

        # evento de saída
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            sys.exit(0)

        # barra da esquerda
        if pygame.key.get_pressed()[pygame.K_w]:
            self.barra_esquerda.mover_pra_cima()
        elif pygame.key.get_pressed()[pygame.K_s]:
            self.barra_esquerda.mover_pra_baixo()
        else:
            self.barra_esquerda.parar()

        # barra da direita
        if pygame.key.get_pressed()[pygame.K_i]:
            self.barra_direita.mover_pra_cima()
        elif pygame.key.get_pressed()[pygame.K_k]:
            self.barra_direita.mover_pra_baixo()
        else:
            self.barra_direita.parar()

    def atualiza_estado(self):
        self.barra_esquerda.atualizar_posicao()
        self.barra_direita.atualizar_posicao()
        self.bola.atualizar_posicao_x()
        self.bola.atualizar_posicao_y()
        self.bola.colisao_esqueda()

    def desenha(self):
        self.tela.fill((255, 255, 255))
        self.barra_direita.desenha(self.tela)
        self.barra_esquerda.desenha(self.tela)
        self.bola.desenha(self.tela)
        pygame.display.flip()


def main():
    jogo = Jogo()
    jogo.rodar()


if __name__ == '__main__':
    main()
