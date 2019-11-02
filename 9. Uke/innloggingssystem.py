from bruker import Bruker

class Innloggingssystem:
    def __init__(self):
        self._brukere = []

    def registrerBruker(self):
        brukernavn = input("Ditt brukernavn: ")
        passord = input("Ditt passord: ")
        self._brukere.append(Bruker(brukernavn, passord))

    def skrivAlleBrukere(self):
        for bruker in self._brukere:
            print(bruker)

    def lastInnFraFil(self):
        fil = open("brukere.csv", "r+", encoding="utf8")
        for linje in fil:
            if "," in linje:
                brukernavn, passord = linje.split(",")
                self._brukere.append(Bruker(brukernavn, passord))
        fil.close()

    def skrivTilFil(self):
        fil = open("brukere.csv", "w", encoding="utf8")
        for bruker in self._brukere:
            fil.write(bruker.hentBrukernavn())
            fil.write(",")
            fil.write(bruker.hentPassord())
            fil.write("\n")

        fil.close()
