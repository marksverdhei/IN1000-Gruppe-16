import random


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
            liste = []
            for j in range(self._bredde):
                if random.randint(1, 10) > 1:
                    liste.append(" ")
                else:
                    liste.append("█")
                
            self._rutenett.append(liste)
        
    def oppdaterLand(self):
        vannTilLand = []
        for rad in range(self._hoyde):
            for kol in range(self._bredde):
                if self._rutenett[rad][kol] == " ":
                    if self.finnNabo(rad, kol).count("█") > 1:
                        vannTilLand.append((rad, kol))
                        
        for rad, kol in vannTilLand:
            self._rutenett[rad][kol] = "█"
            
    def settSkatt(self):
        muligeSteder = []
        for rad in range(self._hoyde):
            for kol in range(self._bredde):
                if self._rutenett[rad][kol] == "█":
                    if self.finnNabo(rad, kol).count("█") == 8:
                        muligeSteder.append((rad, kol))
                        
        if muligeSteder:            
            sRad, sKol = random.choice(muligeSteder)
            self._rutenett[sRad][sKol] = "X"
        
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
            
    def skrivUt(self):
        print(" "+"-" * self._bredde)
        for i in self._rutenett:
            print("|"+"".join(i)+"|")
        print(" "+"-" * self._bredde)    
