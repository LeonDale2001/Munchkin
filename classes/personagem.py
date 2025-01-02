# personagem.py

class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.nivel = 1  # Exemplo de atributo do personagem

    def __str__(self):
        return self.nome
