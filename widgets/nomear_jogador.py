import pygame

class NomearJogador:
    def __init__(self, font_size, cor_texto, cor_borda):
        """
        Inicializa o widget NomearJogador com parâmetros personalizados.

        :param font_size: O tamanho da fonte para o texto.
        :param cor_texto: A cor do texto.
        :param cor_borda: A cor da borda do texto.
        """
        self.font_size = font_size
        self.cor_texto = cor_texto
        self.cor_borda = cor_borda
        # Inicializa a fonte para o texto
        self.font = pygame.font.SysFont('Impact', self.font_size)

    def desenhar(self, screen, jogador_atual, novo_nome, largura_tela, altura_tela):
        """
        Desenha o nome do jogador atual na tela, com borda e centralizado.

        :param screen: A superfície onde o texto será desenhado.
        :param jogador_atual: O índice do jogador atual.
        :param novo_nome: O nome atual do jogador.
        :param largura_tela: Largura da tela.
        :param altura_tela: Altura da tela.
        """
        texto_nome_atual = self.font.render(f"Nome do Jogador {jogador_atual + 1}: {novo_nome}", True, self.cor_texto)
        texto_borda = self.font.render(f"Nome do Jogador {jogador_atual + 1}: {novo_nome}", True, self.cor_borda)

        # Calcula a posição central
        x_nome_atual = (largura_tela - texto_nome_atual.get_width()) * 0.5
        y_nome_atual = (altura_tela - texto_nome_atual.get_height()) * 0.25

        # Desenha a borda (Texto branco)
        screen.blit(texto_borda, (x_nome_atual + 2, y_nome_atual + 2))  # Desloca um pouco para criar o efeito de borda

        # Desenha o texto (Texto da cor definida)
        screen.blit(texto_nome_atual, (x_nome_atual, y_nome_atual))