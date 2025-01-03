# main.py
import pygame
from controller import Controller

# Inicializa o Pygame
pygame.init()

# Define as dimensões da tela
largura, altura = 1920, 1000

# Cria o controlador
controller = Controller(largura, altura)

# Executa o controlador
controller.executar()

# Encerra o Pygame
pygame.quit()
