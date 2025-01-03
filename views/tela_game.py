# tela_game.py
import pygame
import sys
from widgets.back_arrow import BackArrow  # Certifique-se de que a classe BackArrow está sendo importada

class TelaGame:
    def __init__(self, largura, altura, jogadores):
        self.largura = largura
        self.altura = altura
        self.tela = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption("Tela de Jogo")

        # Carregar o fundo (se necessário)
        self.background = pygame.image.load('assets/bg.jpg')
        self.background = pygame.transform.scale(self.background, (largura, altura))

        # Armazenar os dados dos jogadores
        self.jogadores = jogadores

        # Criar o back arrow no canto superior esquerdo
        self.back_arrow = BackArrow('assets/back_arrow.png', 40, 40, self.largura - 50, 10)

    def desenhar_tela(self):
        # Desenha o fundo
        self.tela.blit(self.background, (0, 0))

        # Desenha o back arrow
        self.back_arrow.desenhar(self.tela)

        # Exibir os jogadores (se necessário, para depuração)
        font = pygame.font.Font(None, 40)
        for i, jogador in enumerate(self.jogadores):
            texto = font.render(f"Jogador {i + 1}: {jogador['nome']}", True, (255, 255, 255))
            self.tela.blit(texto, (50, 100 + i * 50))

        # Atualiza a tela
        pygame.display.flip()

    def checar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = evento.pos
                if self._verificar_clique_seta(pos_mouse):
                    return False  # Retorna False para voltar à TelaName

        return True

    def _verificar_clique_seta(self, pos_mouse):
        x, y = pos_mouse
        if self.back_arrow.pos_x <= x <= self.back_arrow.pos_x + self.back_arrow.largura and \
           self.back_arrow.pos_y <= y <= self.back_arrow.pos_y + self.back_arrow.altura:
            return True
        return False
