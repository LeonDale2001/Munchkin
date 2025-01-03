from classes.carta import Carta


class Monstro(Carta):
    def __init__(self, nome, nivel, recompensa, penalidade):
        super().__init__(nome, "Monstro")
        self.nivel = nivel
        self.recompensa = recompensa
        self.penalidade = penalidade
