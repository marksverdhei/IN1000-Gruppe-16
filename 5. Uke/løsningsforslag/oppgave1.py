
navneliste = ["Marte", "Hans", "Geir"]
tallliste = []
# a) tegn opp listene etter at følgende kode har kjørt:

navneliste.append("Heidi")
tallliste.append(7)
tallliste.append(0)
tallliste.append(4)
tallliste.append(-3)
tallliste.append(43)

print(navneliste, tallliste, "\n", sep="\n")

print(navneliste[1])
print(tallliste[2])

navneliste.remove("Hans")
tallliste.pop()
tallliste.pop(0)

print("\n", navneliste, tallliste, "\n", sep="\n")

# print(tallliste)
print(len(navneliste))
print(tallliste[0])
print(4 in tallliste)
print(5 in tallliste)
sumToForste = tallliste[0] + tallliste[1]
print(sumToForste)

for i in navneliste:
    print(i)

for i in tallliste:
    print(i)
