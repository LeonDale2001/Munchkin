# jogador.py
from classes.personagem import Personagem  # Importa a classe Personagem

class Jogador:
    def __init__(self, nome, personagem):
        self.nome = nome
        self.personagem = personagem

    def __str__(self):
        return f"{self.nome} ({self.personagem.nome})"
