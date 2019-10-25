from skattekart import Skattekart

hoyde = int(input("Høyde: "))
bredde = int(input("Bredde: "))
kart = Skattekart(hoyde, bredde)
kart.skrivUt()