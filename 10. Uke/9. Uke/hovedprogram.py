from innloggingssystem import Innloggingssystem

def hovedprogram():
    mittSystem = Innloggingssystem()
    mittSystem.lastInnFraFil()

    alternativer = ["[1] Registrer ny bruker", "[2] Se alle brukere",
                    "[0] Lagre og avslutt program"]

    svar = "1"

    while svar != "0":
        for i in alternativer:
            print(i)

        svar = input(">")
        if svar == "1":
            mittSystem.registrerBruker()
        elif svar == "2":
            mittSystem.skrivAlleBrukere()
        elif svar != "0":
            print("Ugyldig input!")

    mittSystem.skrivTilFil()

hovedprogram()
