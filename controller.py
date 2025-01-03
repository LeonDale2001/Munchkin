# controller.py
import pygame
from views.tela_ini import TelaInicial
from views.tela_name import TelaName
from views.tela_game import TelaGame  # Importando TelaGame

class Controller:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.rodando = True

        # Criação da tela inicial
        self.tela_inicial = TelaInicial(self.largura, self.altura)
        self.tela_nome = None  # TelaName ainda não foi criada
        self.tela_jogo = None  # TelaGame ainda não foi criada

    def executar(self):
        while self.rodando:
            # Controla o fluxo de telas
            if self.tela_nome is None and self.tela_jogo is None:
                # Exibe a Tela Inicial e aguarda a seleção de jogadores
                self._tela_inicial()
            elif self.tela_nome is not None:
                # Exibe a Tela de Nome
                self._tela_nome()
            elif self.tela_jogo is not None:
                # Exibe a Tela de Jogo
                self._tela_jogo()

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
                    # Quando clicar em "Jogar", vai para a Tela de Nome
                    quantidade_jogadores = self.tela_inicial.get_quantidade_jogadores()
                    self.tela_nome = TelaName(self.largura, self.altura, quantidade_jogadores)

        # Atualiza a tela
        pygame.display.flip()

    def _tela_nome(self):
        # Desenha a tela de Nome
        self.tela_nome.desenhar_tela()

        # Verifica os eventos na Tela de Nome
        if not self.tela_nome.checar_eventos():
            # Quando clicar na seta de voltar, volta para a Tela Inicial
            self.tela_nome = None  # Limpa a Tela de Nome para voltar à Tela Inicial
        elif self.tela_nome.jogador_atual == self.tela_nome.jogadores_selecionados:
            # Quando todos os jogadores tiverem sido nomeados, vai para a Tela de Jogo
            self.tela_jogo = TelaGame(self.largura, self.altura, self.tela_nome.jogadores)
            self.tela_nome = None  # Limpa a Tela de Nome para a transição para a Tela de Jogo

        # Atualiza a tela
        pygame.display.flip()

    def _tela_jogo(self):
        # Desenha a tela de Jogo
        self.tela_jogo.desenhar_tela()

        # Verifica os eventos na Tela de Jogo
        if not self.tela_jogo.checar_eventos():
            # Quando clicar no back arrow, volta para a TelaName
            self.tela_jogo = None  # Limpa a Tela de Jogo para voltar à Tela de Nome

        # Atualiza a tela
        pygame.display.flip()
