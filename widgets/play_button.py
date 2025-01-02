import pygame

class PlayButton:
    def __init__(self, x, y, largura, altura, texto, fonte, raio_borda=10):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.cor_botao = (255, 0, 0)  # Cor do botão
        self.cor_borda = (255, 255, 255)  # Cor da borda
        self.cor_texto = (255, 255, 255)  # Cor do texto
        self.texto = texto
        self.fonte = fonte
        self.raio_borda = raio_borda
        self.selecionado = False

    def desenhar(self, tela):
        # Se o botão estiver selecionado, muda a cor de fundo e da borda
        if self.selecionado:
            cor_botao = (0, 255, 0)  # Cor de fundo verde
            cor_borda = (255, 255, 255)  # Borda branca
            cor_texto = (255, 255, 255)  # Cor do texto branco
        else:
            cor_botao = self.cor_botao  # Cor original do botão
            cor_borda = self.cor_borda  # Cor original da borda
            cor_texto = (255, 255, 255)  # Cor do texto branco quando não selecionado

        # Desenha a borda com cantos arredondados
        pygame.draw.rect(tela, cor_borda, (self.x, self.y, self.largura, self.altura), 5, border_radius=self.raio_borda)

        # Desenha o corpo do botão com cantos arredondados
        pygame.draw.rect(tela, cor_botao, (self.x + 5, self.y + 5, self.largura - 10, self.altura - 10), border_radius=self.raio_borda)

        # Renderiza o texto no botão com a cor alterada
        texto_renderizado = self.fonte.render(self.texto, True, cor_texto)
        texto_rect = texto_renderizado.get_rect(center=(self.x + self.largura // 2, self.y + self.altura // 2))
        tela.blit(texto_renderizado, texto_rect)

    def clicar(self, pos_mouse):
        """Verifica se o botão foi clicado."""
        if self.x <= pos_mouse[0] <= self.x + self.largura and self.y <= pos_mouse[1] <= self.y + self.altura:
            return True
        return False
