import pygame
import sys
from widgets.nomear_jogador import NomearJogador  # Importe a classe NomearJogador
from widgets.jogador_i import JogadorI  # Importe a nova classe Jogador

class TelaPlay:
    def __init__(self, largura, altura, jogadores_selecionados):
        # Inicializa a tela
        self.largura = largura
        self.altura = altura
        self.tela = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption("Tela de Jogo")

        # Carrega o fundo
        self.background = pygame.image.load('assets/bg.jpg')
        self.background = pygame.transform.scale(self.background, (largura, altura))

        # Número de jogadores selecionados
        self.jogadores_selecionados = jogadores_selecionados

        # Lista para armazenar os jogadores e seus respectivos níveis
        self.jogadores = [{"nome": "", "nivel": 0} for _ in range(jogadores_selecionados)]
        self.jogador_atual = 0  # Controla qual jogador está sendo nomeado
        self.novo_nome = ""

        # Fonte para exibir os nomes dos jogadores
        self.font = pygame.font.SysFont('Arial', 30)  # Inicializa a fonte aqui

        # Cria uma instância de NomearJogador com os parâmetros desejados
        self.nomear_jogador_widget = NomearJogador(font_size=40, cor_texto=(255, 0, 0), cor_borda=(255, 255, 255))
        
        # Cria a instância da classe Jogador com as novas configurações
        self.jogador_widget = JogadorI(font_size=30, cor_texto=(255, 255, 255), cor_borda=(255, 0, 0))

    def desenhar_tela(self):
        # Desenha o fundo
        self.tela.blit(self.background, (0, 0))

        # Exibe o nome do jogador atual chamando o método desenhar da classe NomearJogador
        self.nomear_jogador_widget.desenhar(self.tela, self.jogador_atual, self.novo_nome, self.largura, self.altura)

        # Exibe os nomes dos jogadores abaixo de "Nome do Jogador"
        for i, jogador in enumerate(self.jogadores):
            self.jogador_widget.desenhar(self.tela, jogador["nome"], i, self.largura, self.altura)

        # Atualiza a tela
        pygame.display.flip()

    def checar_eventos(self):
        # Checa os eventos da tela
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                # Se o jogador clicar no X da janela, termina o jogo
                pygame.quit()
                sys.exit()  # Fecha a aplicação

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:
                    # Remove o último caractere do nome atual
                    self.novo_nome = self.novo_nome[:-1]
                elif evento.key == pygame.K_RETURN:
                    # Se o nome atual não estiver vazio, confirma o nome e passa para o próximo jogador
                    if self.novo_nome != "" and self.jogador_atual < self.jogadores_selecionados:
                        self.jogadores[self.jogador_atual]["nome"] = self.novo_nome
                        self.jogador_atual += 1
                        self.novo_nome = ""

                    # Se todos os jogadores forem nomeados, não faz mais nada
                    if self.jogador_atual == self.jogadores_selecionados:
                        print("Jogadores e Níveis definidos:")
                        for jogador in self.jogadores:
                            print(f"{jogador['nome']} - Nível {jogador['nivel']}")
                        # Não faz nada, apenas retorna True para continuar o jogo
                        return True
                else:
                    # Adiciona o caractere pressionado ao nome atual
                    if self.jogador_atual < self.jogadores_selecionados:
                        self.novo_nome += evento.unicode

        return True  # Continua nomeando jogadores
