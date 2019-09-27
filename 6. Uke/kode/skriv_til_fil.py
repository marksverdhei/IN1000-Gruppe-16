fil = open("minfil.txt", encoding="utf8")
print(fil.read())
fil.close()

fil = open("minfil.txt", "a", encoding="utf8")
fil.write(input("Skriv inn det du vil legge til: "))
fil.close()
