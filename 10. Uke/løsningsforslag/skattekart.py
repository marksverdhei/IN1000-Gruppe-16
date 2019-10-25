import random
hav = " "
land = "█"
skatt = "X"

class Skattekart:
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
                    rad.append(" ")
                else:
                    rad.append("█")
            self._rutenett.append(rad)
        
    def oppdaterLand(self):
        landKordinater = []
        for i in range(self._hoyde):
            for j in range(self._bredde):
                if self._rutenett[i][j] == " ":
                    if self.finnNabo(i, j).count("█") > 1:
                        landKordinater.append((i, j))
                        
        for i, j in landKordinater:
            self._rutenett[i][j] = "█"
    
    def settSkatt(self):
        irange = list(range(self._hoyde))
        random.shuffle(irange)
        jrange = list(range(self._bredde))
        random.shuffle(jrange)
        
        for i in irange:
            for j in jrange:
                if self._rutenett[i][j] == "█":
                    if self.finnNabo(i, j).count(" ") == 0:
                        self._rutenett[i][j] = "X"
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
# kart.skrivUt()
print(kart._rutenett)