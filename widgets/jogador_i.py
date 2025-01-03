import pygame

class JogadorI:
    def __init__(self, font_size, cor_texto, cor_borda):
        """
        Inicializa o widget Jogador com parâmetros personalizados.

        :param font_size: O tamanho da fonte para o texto.
        :param cor_texto: A cor do texto.
        :param cor_borda: A cor da borda do texto.
        """
        self.font_size = font_size
        self.cor_texto = cor_texto
        self.cor_borda = cor_borda
        # Inicializa a fonte para o texto dos jogadores
        self.font = pygame.font.SysFont('Impact', self.font_size)

    def desenhar(self, screen, nome_jogador, index, largura_tela, altura_tela):
        """
        Desenha o nome do jogador na tela, com borda e centralizado na posição especificada.

        :param screen: A superfície onde o texto será desenhado.
        :param nome_jogador: O nome do jogador.
        :param index: O índice do jogador (Jogador 1, Jogador 2, etc.).
        :param largura_tela: Largura da tela.
        :param altura_tela: Altura da tela.
        """
        texto_nome = self.font.render(f"Jogador {index + 1}: {nome_jogador}", True, self.cor_texto)
        texto_borda = self.font.render(f"Jogador {index + 1}: {nome_jogador}", True, self.cor_borda)

        # Calcula a posição abaixo de "Nome do Jogador"
        x_nome_jogador = (largura_tela - texto_nome.get_width()) * 0.5
        y_nome_jogador = altura_tela * 0.35 + (index * 40)

        # Desenha a borda (Texto vermelho)
        screen.blit(texto_borda, (x_nome_jogador + 2, y_nome_jogador + 2))  # Desloca um pouco para criar o efeito de borda

        # Desenha o nome do jogador na tela
        screen.blit(texto_nome, (x_nome_jogador, y_nome_jogador))
