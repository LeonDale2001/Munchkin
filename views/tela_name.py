# tela_name.py
import pygame
import sys
from widgets.nomear_jogador import NomearJogador
from widgets.jogador_i import JogadorI
from widgets.back_arrow import BackArrow

class TelaName:
    def __init__(self, largura, altura, jogadores_selecionados):
        self.largura = largura
        self.altura = altura
        self.tela = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption("Tela de Nomear")
        
        # Certifique-se de que a imagem do fundo está sendo carregada corretamente
        self.background = pygame.image.load('assets/bg.jpg')
        self.background = pygame.transform.scale(self.background, (largura, altura))

        # Restante do código de inicialização
        self.jogadores_selecionados = jogadores_selecionados
        self.jogadores = [{"nome": "", "nivel": 0} for _ in range(jogadores_selecionados)]
        self.jogador_atual = 0
        self.novo_nome = ""
        self.nomear_jogador_widget = NomearJogador(font_size=40, cor_texto=(255, 0, 0), cor_borda=(255, 255, 255))
        self.jogador_widget = JogadorI(font_size=30, cor_texto=(255, 255, 255), cor_borda=(255, 0, 0))
        self.back_arrow = BackArrow('assets/back_arrow.png', 40, 40, self.largura - 50, 10)

    def desenhar_tela(self):
        self.tela.blit(self.background, (0., 0))
        self.back_arrow.desenhar(self.tela)
        self.nomear_jogador_widget.desenhar(self.tela, self.jogador_atual, self.novo_nome, self.largura, self.altura)
        for i, jogador in enumerate(self.jogadores):
            self.jogador_widget.desenhar(self.tela, jogador["nome"], i, self.largura, self.altura)
        pygame.display.flip()

    def checar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.K_ESCAPE:
                return False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if self._verificar_clique_seta(evento.pos):
                    return False  # Retorna False para voltar à TelaInicial
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:
                    self.novo_nome = self.novo_nome[:-1]
                elif evento.key == pygame.K_RETURN:
                    if self.novo_nome != "" and self.jogador_atual < self.jogadores_selecionados:
                        self.jogadores[self.jogador_atual]["nome"] = self.novo_nome
                        self.jogador_atual += 1
                        self.novo_nome = ""
                    if self.jogador_atual == self.jogadores_selecionados:
                        print("Jogadores e Níveis definidos:")
                        for jogador in self.jogadores:
                            print(f"{jogador['nome']} - Nível {jogador['nivel']}")
                        return True
                else:
                    if self.jogador_atual < self.jogadores_selecionados:
                        self.novo_nome += evento.unicode
        return True

    def _verificar_clique_seta(self, pos_mouse):
        x, y = pos_mouse
        if self.back_arrow.pos_x <= x <= self.back_arrow.pos_x + self.back_arrow.largura and \
           self.back_arrow.pos_y <= y <= self.back_arrow.pos_y + self.back_arrow.altura:
            return True
        return False
