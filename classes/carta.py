class Carta:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

    def __str__(self):
        return f"{self.nome} ({self.tipo})"