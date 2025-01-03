# controller.py
import pygame
from view.tela_ini import TelaInicial
from view.tela_play import TelaPlay

class Controller:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.rodando = True

        # Criação da tela inicial
        self.tela_inicial = TelaInicial(self.largura, self.altura)
        self.tela_play = None  # TelaPlay ainda não foi criada

    def executar(self):
        while self.rodando:
            # Controla o fluxo de telas
            if self.tela_play is None:
                # Exibe a Tela Inicial e aguarda a seleção de jogadores
                self._tela_inicial()
            else:
                # Exibe a Tela de Jogo
                self._tela_play()

    def _tela_inicial(self):
        # Desenha a tela inicial
        self.tela_inicial.desenhar_tela()

        # Verifica os eventos na tela inicial
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.rodando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = evento.pos
                if self.tela_inicial.checar_click(pos_mouse):
                    # Quando clicar em "Jogar", vai para a Tela de Jogo
                    quantidade_jogadores = self.tela_inicial.get_quantidade_jogadores()
                    self.tela_play = TelaPlay(self.largura, self.altura, quantidade_jogadores)

        # Atualiza a tela
        pygame.display.flip()

    def _tela_play(self):
        # Desenha a tela de jogo
        self.tela_play.desenhar_tela()

        # Verifica os eventos na Tela de Jogo
        if not self.tela_play.checar_eventos():
            # Quando clicar na seta de voltar, volta para a Tela Inicial
            self.tela_play = None  # Limpa a Tela de Jogo para voltar à Tela Inicial

        # Atualiza a tela
        pygame.display.flip()

