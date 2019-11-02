class Spillebrett:
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._rutenett = []
        self._generer()
        
    def tegnBrett(self):
        for rad in self._rutenett:
            for celle in rad:
                print(celle.hentStatusTegn())
            print()
        
    def oppdatering(self):
        pass
        
    def finnAntallLevende(self):
        pass
        
    def _generer(self):
        for i in range(self._rader):
            rad = []
            for j in range(self._kolonner):
                rad.append(Celle())
            self._rutenett.append(rad)
        
    def finnNabo(self, rad, kol):
        naboliste = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                gyldig = False
                if rad+i in range(self._hoyde):
                    if kol+j in range(self._bredde):
                        if i != 0 or j != 0:
                            gyldig = True
                
                if gyldig:
                    naboliste.append(self._rutenett[rad+i][kol+j])
        
        return naboliste
