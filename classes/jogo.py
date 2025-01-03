from classes import baralho
from classes.combate import Combate
from classes.monstro import Monstro

class Jogo:
    def __init__(self):
        self.jogadores = []
        self.baralho_porta = baralho.Baralho()
        self.baralho_tesouro = baralho.Baralho()

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    def iniciar_turno(self):
        for jogador in self.jogadores:
            print(f"Turno de {jogador.nome}")
            carta = self.baralho_porta.puxar_carta()
            if isinstance(carta, Monstro):
                combate = Combate(jogador, carta)
                combate.iniciar_combate()
            else:
                print(f"{jogador.nome} encontrou uma carta: {carta}")