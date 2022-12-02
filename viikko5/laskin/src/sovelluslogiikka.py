class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos

class Summa:
    def __init__(self, sovellus, arvo):
        self.sovellus = sovellus
        self.arvo = arvo

    def suorita(self):
        tulos = self.sovellus.tulos + self.arvo()
        self.sovellus.tulos = tulos

class Erotus:
    def __init__(self, sovellus, arvo):
        self.sovellus = sovellus
        self.arvo = arvo

    def suorita(self):
        tulos = self.sovellus.tulos - self.arvo()
        self.sovellus.tulos = tulos

class Nollaus:
    def __init__(self, sovellus, arvo):
        self.sovellus = sovellus
        self.arvo = arvo

    def suorita(self):
        self.sovellus.tulos = 0

class Kumoa:
    def __init__(self, sovellus, arvo):
        self.sovellus = sovellus
        self.arvo = arvo

    def suorita(self):
        pass
