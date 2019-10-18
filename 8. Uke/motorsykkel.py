class Motorsykkel:
    def __init__(self, merke, regNr, km):
        self._merke = merke
        self._regNr = regNr
        self._km = km

    def kjor(self, km):
        self._km += km

    def hentKilometerstand(self):
        return self._km

    def hentRegNr(self):
        return self._regNr

    def skrivUt(self):
        print("Merke:", self._merke)
        print("Registreringsnummer:", self._regNr)
        print("Kilometerstand:", self._km)


    def __eq__(self, other):
        return self.hentRegNr() == other.hentRegNr()

Motorsykkel("", "123", 0) == Motorsykkel("", "123", 0)
Motorsykkel("", "123", 0) is Motorsykkel("", "123", 0)
