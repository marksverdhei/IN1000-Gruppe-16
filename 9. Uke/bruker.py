
class Bruker:
    def __init__(self, brukernavn, passord):
        self._brukernavn = brukernavn
        self._passord = passord

    def hentBrukernavn(self):
        return self._brukernavn

    def hentPassord(self):
        return self._passord

    def __str__(self):
        return "bruker: " + self._brukernavn
