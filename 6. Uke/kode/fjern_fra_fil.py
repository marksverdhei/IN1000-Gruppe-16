
# lagre alt i filen i en liste
fil = open("gjesteliste.txt", "r", encoding="utf8")
gjester = list(fil)
fil.close()
# fjern tredje linje
gjester.pop(2)

# skriv listen til fil
fil = open("gjesteliste.txt", "w", encoding="utf8")
fil.write("".join(gjester))
fil.close()
