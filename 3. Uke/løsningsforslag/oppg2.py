# Oppgave 2
# Kjør programmet for å få svaret:

liste = [0]

liste1 = [1, 2, 3]

liste2 = [3, 3, 5, 7]

liste3 = ["A", "BC", "D", "E", "F"]

liste4 = ["mange elementer i denne listen"]

liste5 = []

print(liste3[4])
print(liste1[0])
print("liste4[1] - gir oss en feilmelding fordi listen er for kort!")
print("liste3[5] - gir oss en feilmelding fordi listen er for kort! ")

input("\n2.2 (Trykk enter for å fortsette)\n")

print("5 ligger på indeks:", liste2.index(5),"i liste2")
print("'BC' ligger på indeks:", liste3.index("BC"),"i liste3")
print("1 ligger på indeks:", liste1.index(1),"i liste1")
print("'E' ligger på indeks:", liste3.index("E"),"i liste3")

input("\n2.3 (Trykk enter for å fortsette)\n")


# Fremstiller tabellen som en ordbok
tabell = {0 : "'A'",
          1 : "'BC'",
          2 : "'D'",
          3 : "'E'"}

print("Indeks: | verdi:")
for k in tabell:
    print(k, "      |", tabell[k])
