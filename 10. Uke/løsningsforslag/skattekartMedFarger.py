import random


class Skattekart:
    _hav = "\u001b[34;1m█\u001b[0m"
    _land = "\u001b[33;1m█\u001b[0m"
    _skatt = "\u001b[43m\u001b[31mX\u001b[0m"
    def __init__(self, hoyde, bredde):
        self._hoyde = hoyde
        self._bredde = bredde
        self._rutenett = []
        self.genererKart()
        self.oppdaterLand()
        self.settSkatt()
        
        
    def genererKart(self):
        for i in range(self._hoyde):
            rad = []
            for j in range(self._bredde):
                if random.randint(1, 10) > 1:
                    rad.append(self._hav)
                else:
                    rad.append(self._land)
            self._rutenett.append(rad)
        
    def oppdaterLand(self):
        landKordinater = []
        for i in range(self._hoyde):
            for j in range(self._bredde):
                if self._rutenett[i][j] == self._hav:
                    if self.finnNabo(i, j).count(self._land) > 1:
                        landKordinater.append((i, j))
                        
        for i, j in landKordinater:
            self._rutenett[i][j] = self._land
    
    def settSkatt(self):
        irange = list(range(self._hoyde))
        random.shuffle(irange)
        jrange = list(range(self._bredde))
        random.shuffle(jrange)
        
        for i in irange:
            for j in jrange:
                if self._rutenett[i][j] == self._land:
                    if self.finnNabo(i, j).count(self._hav) == 0:
                        self._rutenett[i][j] = self._skatt
                        return
        
    def finnNabo(self, rad, kol):
        naboer = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                gyldig = False
                if rad+i in range(hoyde):
                    if kol+j in range(bredde):
                        if rad != 0 or kol != 0:
                            gyldig = True
                
                if gyldig:
                    naboer.append(self._rutenett[rad+i][kol+j])
                    
        return naboer
        
    def skrivUt(self):
        print(" " + "-" * self._bredde)
        for i in self._rutenett:
            print("|" + "".join(i) + "|")
        print(" " + "-" * self._bredde)
        
hoyde = int(input("Skriv høyde: "))
bredde = int(input("Skriv bredde: "))
kart = Skattekart(hoyde, bredde)
kart.skrivUt()