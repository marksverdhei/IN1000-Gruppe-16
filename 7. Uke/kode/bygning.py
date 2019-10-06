
class Bygning:
    def __init__(self, addr, eier):
        self._addr = addr
        self._eier = eier
        self._leietagere = []

    def legg_til_leietager(self, leietager):
        self._leietagere.append(leietager)

    def skriv_leietagere(self):
        print(self._leietagere)

    def fjern_leietager(self):
        self._leietagere.pop(0)

    def fjern_leietager_paa_navn(self, navn):
        self._leietagere.remove(navn)

bygning1 = Bygning("Karl Johans gate 4", "Pål")

bygning1.legg_til_leietager("Mia")
bygning1.legg_til_leietager("Espen")
bygning1.legg_til_leietager("Mari")
bygning1.legg_til_leietager("Gunnar")
bygning1.skriv_leietagere()

bygning1.fjern_leietager()

bygning1.skriv_leietagere()

bygning1.fjern_leietager_paa_navn("Gunnar")

bygning1.skriv_leietagere()
