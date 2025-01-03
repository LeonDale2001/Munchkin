import pygame

class BackArrow:
    def __init__(self, img_path, largura, altura, pos_x, pos_y):
        """
        Inicializa a seta de volta com a imagem e parâmetros fornecidos.

        :param img_path: Caminho da imagem para a seta de voltar.
        :param largura: Largura da seta.
        :param altura: Altura da seta.
        :param pos_x: Posição X da seta na tela.
        :param pos_y: Posição Y da seta na tela.
        """
        self.img_path = img_path
        self.largura = largura
        self.altura = altura
        self.pos_x = pos_x
        self.pos_y = pos_y
        
        # Carrega e redimensiona a imagem com as dimensões fornecidas
        self.img = pygame.image.load(self.img_path)
        self.img = pygame.transform.scale(self.img, (self.largura, self.altura))

    def desenhar(self, tela):
        """
        Desenha a seta na tela na posição e tamanho definidos.

        :param tela: A tela onde a seta será desenhada.
        """
        tela.blit(self.img, (self.pos_x, self.pos_y))

    def set_posicao(self, pos_x, pos_y):
        """
        Atualiza a posição da seta na tela.

        :param pos_x: Nova posição X.
        :param pos_y: Nova posição Y.
        """
        self.pos_x = pos_x
        self.pos_y = pos_y

    def set_tamanho(self, largura, altura):
        """
        Atualiza o tamanho da seta.

        :param largura: Nova largura da seta.
        :param altura: Nova altura da seta.
        """
        self.largura = largura
        self.altura = altura
        self.img = pygame.transform.scale(self.img, (self.largura, self.altura))
