import pygame

class Title:
    def __init__(self, texto, font_name="Georgia", font_size=50, cor_texto=(255, 0, 0), cor_borda=(255, 255, 255)):
        """
        :param texto: O texto que será exibido
        :param font_name: Nome da fonte (default "arial")
        :param font_size: Tamanho da fonte (default 50)
        :param cor_texto: Cor do texto
        :param cor_borda: Cor da borda do texto
        """
        self.texto = texto
        self.font_name = font_name
        self.font_size = font_size
        self.cor_texto = cor_texto
        self.cor_borda = cor_borda
        self.font = pygame.font.SysFont(self.font_name, self.font_size)

    def desenhar(self, tela, x, y):
        # Renderiza o texto com borda branca
        texto_borda = self.font.render(self.texto, True, self.cor_borda)
        texto_normal = self.font.render(self.texto, True, self.cor_texto)

        # Desenha a borda do título (um deslocamento de 2 pixels em cada direção)
        tela.blit(texto_borda, (x - 2, y - 2))  # Borda esquerda superior
        tela.blit(texto_borda, (x + 2, y - 2))  # Borda direita superior
        tela.blit(texto_borda, (x - 2, y + 2))  # Borda esquerda inferior
        tela.blit(texto_borda, (x + 2, y + 2))  # Borda direita inferior

        # Desenha o título normal
        tela.blit(texto_normal, (x, y))
