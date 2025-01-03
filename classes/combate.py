class Combate:
    def __init__(self, jogador, monstro):
        self.jogador = jogador
        self.monstro = monstro

    def calcular_forca_jogador(self):
        return self.jogador.personagem.nivel

    def iniciar_combate(self):
        forca_jogador = self.calcular_forca_jogador()
        if forca_jogador >= self.monstro.nivel:
            print("Jogador venceu o combate!")
            return True
        else:
            print("Jogador perdeu o combate e precisa fugir!")
            return False