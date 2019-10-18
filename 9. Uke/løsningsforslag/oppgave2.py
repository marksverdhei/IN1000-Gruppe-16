class Bil:
    def __init__(self, regnr, type, aarsmodell):
        self._regnr = regnr
        self._type = type
        self._aarsmodell = aarsmodell

Bil("AB580769", "sedan", 2006)
Bil("CD679357", "coupe", 1999)
Bil("UF597696", "lastebil", 2010)

class Koffert:
    def __init__(self, toalettsakerListe, klesListe):
        self._toalettsaker = toalettsakerListe
        self._klaer = klesListe

Koffert(["tannbørste", "tannkrem"], ["sokk"])
Koffert([], ["genser", "lue"])

class Hund:
    def __init__(self, a, b, c):
        self._alder = a
        self._rase = b
        self._bjefferMye = c

Hund(1, "golden retriever", True)
Hund(10, "labrador", False)
