import pygame
from view.tela_ini import TelaInicial
from view.tela_play import TelaPlay

# Inicializa o Pygame
pygame.init()

# Define as dimensões da tela
largura, altura = 800, 600

# Criação da tela inicial
tela_inicial = TelaInicial(largura, altura)

# Loop principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        # Se o jogador fechar a janela
        if evento.type == pygame.QUIT:
            rodando = False
        
        # Verifica se o mouse foi clicado na tela inicial
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            pos_mouse = evento.pos
            if tela_inicial.checar_click(pos_mouse):
                # Passa a quantidade de jogadores para a tela de jogo
                tela_play = TelaPlay(largura, altura, tela_inicial.get_quantidade_jogadores())

                # Loop da tela de jogo
                while True:
                    tela_play.desenhar_tela()
                    if not tela_play.checar_eventos():
                        rodando = False
                        break

    # Desenha a tela inicial
    tela_inicial.desenhar_tela()

    # Atualiza a tela
    pygame.display.flip()

# Encerra o Pygame
pygame.quit()
