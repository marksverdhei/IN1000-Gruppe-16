import random


class Skattekart:
    _hav = "\u001b[44m \u001b[0m"
    _land = "\u001b[43;1m \u001b[0m"
    _skatt = "\u001b[43;1m\u001b[31mX\u001b[0m"
    
    def __init__(self, hoyde, bredde, landmasse=2, antallSkatter=1):
        self._hoyde = hoyde
        self._bredde = bredde
        self._rutenett = []
        self._genererKart()
        
        for i in range(landmasse):
            self._oppdaterLand()
            
        for i in range(antallSkatter):    
            self._settSkatt()
        
        
    def _genererKart(self):
        for i in range(self._hoyde):
            rad = []
            for j in range(self._bredde):
                if random.randint(1, 10) == 1:
                    rad.append(self._land)
                else:
                    rad.append(self._hav)
            self._rutenett.append(rad)
        
    def _oppdaterLand(self):
        landKordinater = []
        for i in range(self._hoyde):
            for j in range(self._bredde):
                if self._rutenett[i][j] == self._hav:
                    if self.finnNabo(i, j).count(self._land) > 1:
                        landKordinater.append((i, j))
                        
        for i, j in landKordinater:
            self._rutenett[i][j] = self._land
    
    def _settSkatt(self):
        muligeSkatter = []
        
        for i in range(self._hoyde):
            for j in range(self._bredde):
                if self._rutenett[i][j] == self._land:
                    naboer = self.finnNabo(i, j)
                    if naboer.count(self._hav) == 0 and naboer.count(self._skatt) == 0:
                        muligeSkatter.append((i, j))
                        
        if muligeSkatter:
            sRad, sKol = random.choice(muligeSkatter)
            self._rutenett[sRad][sKol] = self._skatt
        
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

landmasse = int(input("Skriv inn landmasse: "))
antallskatter = int(input("Skriv inn antall skatter: "))
kart = Skattekart(hoyde, bredde, landmasse, antallskatter)
kart.skrivUt()