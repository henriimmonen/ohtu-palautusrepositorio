from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.kori = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        maara = 0
        for tuote in self.kori:
            maara += tuote.lukumaara()
        return maara
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        if len(self.kori) > 0:
            summa = 0
            for tuote in self.kori:
                summa += tuote.hinta()
            return summa
        return 0
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        lisattava_tuote = Ostos(lisattava)
        loytyi = False

        for tuote in self.kori:
            if lisattava_tuote.tuotteen_nimi() == tuote.tuotteen_nimi():
                tuote.muuta_lukumaaraa(1)
                loytyi = True

        if not loytyi:
            self.kori.append(lisattava_tuote)

    def poista_tuote(self, poistettava: Tuote):
        if len(self.kori) > 0:
            for tuote in self.kori:
                if poistettava.nimi() == tuote.tuotteen_nimi():
                    if tuote.lukumaara() > 1:
                        tuote.muuta_lukumaaraa(-1)
                    else:
                        self.kori.remove(tuote)
        # poistaa tuotteen

    def tyhjenna(self):
        self.kori = []
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.kori
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
