class Lebewesen:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def atmen(self):
        return f"{self.name} atmet."

    def wachsen(self):
        return f"{self.name} wächst."

class Pflanze(Lebewesen):
    def __init__(self, name, alter, wurzeltiefe):
        super().__init__(name, alter)
        self.wurzeltiefe = wurzeltiefe

    def photosynthese(self):
        return f"{self.name} betreibt Photosynthese."

class Blume(Pflanze):
    def __init__(self, name, alter, wurzeltiefe, farbe, duft):
        super().__init__(name, alter, wurzeltiefe)
        self.farbe = farbe
        self.duft = duft

    def blueten_offnen(self):
        return f"Die Blüten von {self.name} öffnen sich in {self.farbe}."
