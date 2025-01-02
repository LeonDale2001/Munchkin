import pygame
from widgets.button import Button
from widgets.title import Title
from widgets.play_button import PlayButton

class TelaInicial:
    def __init__(self, largura, altura):
        # Define as dimensões da tela
        self.largura = largura
        self.altura = altura
        self.tela = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption('Tela Inicial')

        # Carrega e ajusta o fundo
        self.background = pygame.image.load('assets/bg.jpg')
        self.background = pygame.transform.scale(self.background, (largura, altura))

        # Cores dos botões
        self.cor_botao_normal = (200, 200, 200)
        self.cor_botao_selecionado = (255, 0, 0)

        # Propriedades dos botões
        self.largura_botao = 180
        self.altura_botao = 40
        self.espaco_botao = 10

        # Usar a fonte padrão
        self.fonte = pygame.font.SysFont('Impact', 24)

        # Criação do título
        self.titulo = Title("Munchkin", font_size=100, cor_texto=(255, 0, 0), cor_borda=(255, 255, 255))

        # Altura do título
        self.altura_titulo = self.titulo.font.render("Munchkin", True, (255, 0, 0)).get_height()

        # Altura total dos botões
        total_altura_botoes = 4 * self.altura_botao + 3 * self.espaco_botao
        self.total_altura = self.altura_titulo + total_altura_botoes

        # Posições dos botões
        self.x_botao = (largura - self.largura_botao) // 2
        self.y_inicial = (altura - self.total_altura) // 2 + self.altura_titulo + 20

        # Criação dos botões para selecionar a quantidade de jogadores
        self.botoes = [
            Button(self.x_botao, self.y_inicial + i * (self.altura_botao + self.espaco_botao), self.largura_botao, self.altura_botao, 
                   self.cor_botao_normal, self.cor_botao_selecionado, f"{3 + i} JOGADORES", self.fonte, raio_borda=10) 
            for i in range(4)
        ]

        # Marca o primeiro botão como selecionado inicialmente
        self.botoes[0].selecionado = True
        self.selecionado = 0

        # Criação do botão "JOGAR"
        self.botao_jogar = PlayButton(self.x_botao, self.y_inicial + total_altura_botoes + self.espaco_botao, 
                                      self.largura_botao, self.altura_botao, "JOGAR", self.fonte, raio_borda=10)

    def desenhar_tela(self):
        # Desenha o fundo
        self.tela.blit(self.background, (0, 0))

        # Desenha o título
        x_titulo = (self.largura - self.titulo.font.render("Munchkin", True, (255, 0, 0)).get_width()) // 2
        y_titulo = (self.altura - self.total_altura) // 2
        self.titulo.desenhar(self.tela, x_titulo, y_titulo)

        # Desenha os botões
        for botao in self.botoes:
            botao.desenhar(self.tela)

        # Desenha o botão "JOGAR"
        self.botao_jogar.desenhar(self.tela)

        # Atualiza a tela
        pygame.display.flip()

    def checar_click(self, pos_mouse):
        for i, botao in enumerate(self.botoes):
            if botao.clicar(pos_mouse):
                if self.selecionado != i:
                    self.botoes[self.selecionado].selecionado = False
                    self.selecionado = i
                    self.botoes[self.selecionado].selecionado = True

        # Checa se o botão "Jogar" foi clicado
        if self.botao_jogar.clicar(pos_mouse):
            return True
        return False

    def get_quantidade_jogadores(self):
        return self.selecionado + 3  # Retorna a quantidade de jogadores selecionados (3 a 6)
