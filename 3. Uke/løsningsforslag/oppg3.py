from tabell import skriv_tabell

navn = ["Ola", "Martin", "Selma"]

skriv_tabell(navn)

print("\nnavn[1] ==", navn[1], "\n")

navn.insert(0, "Gunnar")
navn.insert(0, "Anna")

skriv_tabell(navn)

navn.remove("Martin")

print("\n", navn[0], navn[1], navn[2], navn[3])
