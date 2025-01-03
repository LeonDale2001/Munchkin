import pygame
import sys

class TelaJogo:
    def __init__(self, largura, altura, jogadores=None):
        pygame.init()
        self.largura = largura
        self.altura = altura
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Munchkin")
        self.relogio = pygame.time.Clock()
        self.rodando = True
        self.jogadores = jogadores if jogadores else []
        self.background = pygame.Surface((self.largura, self.altura))
        self.background.fill((200, 200, 200))

    def desenhar_fundo(self):
        self.tela.blit(self.background, (0, 0))

    def desenhar_elementos(self):
        fonte_titulo = pygame.font.Font(None, 48)
        fonte_normal = pygame.font.Font(None, 36)

        # Título
        titulo = fonte_titulo.render("MUNCHKIN", True, (0, 0, 0))
        self.tela.blit(titulo, (self.largura // 2 - titulo.get_width() // 2, 10))

        # Texto de status
        status = fonte_normal.render("Você derrotou o monstro!", True, (0, 0, 0))
        self.tela.blit(status, (self.largura // 2 - status.get_width() // 2, 70))

        # Cartas de combate
        for i in range(4):
            pygame.draw.rect(self.tela, (255, 255, 255), (150 + i * 120, 200, 100, 150))
            texto_carta = fonte_normal.render("Combate", True, (0, 0, 0))
            self.tela.blit(texto_carta, (150 + i * 120 + 15, 270))

        # Botões de ação
        botoes = ["Atacar", "Fugir", "Usar Item"]
        for i, botao in enumerate(botoes):
            pygame.draw.rect(self.tela, (255, 255, 255), (200 + i * 150, 400, 120, 50))
            texto_botao = fonte_normal.render(botao, True, (0, 0, 0))
            self.tela.blit(texto_botao, (200 + i * 150 + 20, 415))

        # Jogadores
        for i, jogador in enumerate(self.jogadores):
            x = 50 + (i % 3) * 250
            y = 500 + (i // 3) * 100

            pygame.draw.circle(self.tela, (150, 150, 150), (x, y), 40)
            texto_jogador = fonte_normal.render(jogador["nome"], True, (0, 0, 0))
            texto_nivel = fonte_normal.render(f"Nível {jogador['nivel']}", True, (0, 0, 0))

            self.tela.blit(texto_jogador, (x - texto_jogador.get_width() // 2, y + 50))
            self.tela.blit(texto_nivel, (x - texto_nivel.get_width() // 2, y + 80))

    def loop_principal(self):
        while self.rodando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.rodando = False

            self.desenhar_fundo()
            self.desenhar_elementos()
            pygame.display.flip()
            self.relogio.tick(30)

        pygame.quit()

if __name__ == "__main__":
    jogadores = [
        {"nome": "Jogador 1", "nivel": 1},
        {"nome": "Jogador 2", "nivel": 1},
        {"nome": "Jogador 3", "nivel": 1},
        {"nome": "Jogador 4", "nivel": 1},
        {"nome": "Jogador 5", "nivel": 1},
    ]

    tela_jogo = TelaJogo(800, 600, jogadores=jogadores)
    tela_jogo.loop_principal()
