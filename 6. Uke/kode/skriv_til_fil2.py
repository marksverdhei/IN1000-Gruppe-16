
fil = open("gjesteliste.txt", "w", encoding="utf8")

gjester = []
svar = ""
while svar != "q":
    gjester.append(svar)
    svar = input("Hvem vil du invitere til bursdagen din?\n>")

for i in gjester:
    fil.write(i + "\n")

fil.close()
