class Leilighet:
    def __init__(self, nr, etg):
        self._nr = nr
        self._etg = etg

    def hentNummer(self):
        return self.nr

    def hentEtasje(self):
        return self._etg

    def __str__(self):
        return "Leilighet " + str(self._nr) + " i " + str(self._etg) + ". etasje"

print(Leilighet("123", 1))
