class Inventario:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        if len(self.itens) < 5:  # Limite de 5 itens
            self.itens.append(item)
        else:
            print("Inventário cheio!")

    def remover_item(self, item):
        if item in self.itens:
            self.itens.remove(item)
