
class Dyr:
    def __init__(self, art, kjonn, vekt):
        self._art = art
        self._kjonn = kjonn
        self._vekt = vekt

    def hent_art(self):
        return self._art

    def hent_kjonn(self):
        return self._kjonn

    def hent_vekt(self):
        return self._vekt

    def skriv_info(self):
        print(self._art,  "\nKjønn: ", self._kjonn, "\nvekt:", self._vekt)
