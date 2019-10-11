from motorsykkel import Motorsykkel
from garasje import Garasje

kariMotorsykkel = Motorsykkel("BMW", "12345678", 10)

olaMotorsykkel = Motorsykkel("BMW", "22222222", 10)

print(kariMotorsykkel is olaMotorsykkel)
print(kariMotorsykkel == olaMotorsykkel)

minGarasje = Garasje("Dronningens gate 4")
minGarasje.leggTilKjoretoy(kariMotorsykkel)
minGarasje.leggTilKjoretoy(olaMotorsykkel)
minGarasje.skrivGarasje()

print(minGarasje.finnKjoretoy("22222222"))
