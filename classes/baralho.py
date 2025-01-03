class Baralho:
    def __init__(self):
        self.cartas = []

    def adicionar_carta(self, carta):
        self.cartas.append(carta)

    def embaralhar(self):
        import random
        random.shuffle(self.cartas)

    def puxar_carta(self):
        return self.cartas.pop() if self.cartas else None