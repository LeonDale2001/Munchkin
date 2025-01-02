import pygame

class Button:
    def __init__(self, x, y, largura, altura, cor_botao, cor_borda, texto, fonte, raio_borda=10):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.cor_botao = cor_botao
        self.cor_borda = cor_borda
        self.texto = texto
        self.fonte = fonte
        self.raio_borda = raio_borda
        self.selecionado = False

    def desenhar(self, tela):
        # Quando o botão está selecionado, a cor do botão, borda e texto mudam
        if self.selecionado:
            cor_botao = (255, 255, 255) # Cor vermelha
            cor_borda = (255, 0, 0)  # Borda branca
            cor_texto = (255, 0, 0)  # Cor do texto branco quando selecionado
        else:
            # Quando não selecionado, a borda deve ser mais escura
            cor_botao = self.cor_botao
            cor_borda = self.darker_color(self.cor_botao)
            cor_texto = self.darker_color(self.cor_botao)  # Cor preta quando não selecionado

        # Desenha a borda com cantos arredondados
        pygame.draw.rect(tela, cor_borda, (self.x, self.y, self.largura, self.altura), 5, border_radius=self.raio_borda)

        # Desenha o corpo do botão com cantos arredondados
        pygame.draw.rect(tela, cor_botao, (self.x + 5, self.y + 5, self.largura - 10, self.altura - 10), border_radius=self.raio_borda)

        # Renderiza o texto no botão com a nova cor
        texto_renderizado = self.fonte.render(self.texto, True, cor_texto)  # Texto com cor variável
        texto_rect = texto_renderizado.get_rect(center=(self.x + self.largura // 2, self.y + self.altura // 2))  # Centraliza o texto
        tela.blit(texto_renderizado, texto_rect)

    def clicar(self, pos_mouse):
        """Verifica se o botão foi clicado."""
        if self.x <= pos_mouse[0] <= self.x + self.largura and self.y <= pos_mouse[1] <= self.y + self.altura:
            self.selecionado = True  # Marca como selecionado
            return True
        return False

    def desmarcar(self):
        """Desmarca o botão, se necessário.""" 
        self.selecionado = False

    def darker_color(self, cor):
        """Gera uma cor mais escura para a borda com base na cor original do botão."""
        r, g, b = cor
        r = max(0, r - 100)  # Diminuir o valor de vermelho
        g = max(0, g - 100)  # Diminuir o valor de verde
        b = max(0, b - 100)  # Diminuir o valor de azul
        return (r, g, b)
