
fil = open("minfil.txt", encoding="utf8")
handleliste = []

for linje in fil:
    liste_med_ord = linje.split()
    if len(liste_med_ord) == 2:
        handleliste.append(liste_med_ord[1])

print(handleliste)
print(list(fil))

for linje in fil:
    print(linje, end="")

fil.close()
