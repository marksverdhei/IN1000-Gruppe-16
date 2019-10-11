class Garasje:
    def __init__(self, addr):
        self._addresse = addr
        self._motorsykler = []

    def leggTilKjoretoy(self, kjoretoy):
        self._motorsykler.append(kjoretoy)

    def skrivGarasje(self):
        print("Garasje på ", self._addresse)
        print("Motorykler i garasjen:")
        for kjoretoy in self._motorsykler:
            print(kjoretoy)

    def finnKjoretoy(self, regNr):
        for kjoretoy in self._motorsykler:
            if kjoretoy.hentRegNr() == regNr:
                return kjoretoy

        return None
