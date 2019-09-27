# Oppgave 1
def maks(x, y):
    if x > y:
        return x
    else:
        return y

# Oppgave 2

"""Alternativ 1:"""
fil = open("historie.txt", "r", encoding="utf8")
linjer = []
for linje in fil:
    linjer.append(linje)
fil.close()

"""Alternativ 2"""
fil = open("historie.txt", "r", encoding="utf8")
linjer = list(fil)
fil.close()

# Oppgave 3

def min_funksjon(p, q):
    if p and q:
        return 1
    elif not p and not q:
        return 0

# Denne funksjonen tar ikke høyde for hvis
# et av argumentene er sant og et annet er usant

# Oppgave 4

# a)


for i in range(0, 10, 2):
    print(i)

# som vi vet er det tredje argumentet i range
# steget, så i dette tilfellt vil range(0, 10, 2)
# gi sekvensen: 0 -> 2 -> 4 -> 6 -> 8

# b)

sum_partall = sum(range(0, 10, 2))

# c)

sum_oddetall = sum(range(9, 0, -2))

# Oppgave 5

liste = [2, 3, 6, 8]

for i in liste:
    print(i)

# a)
def skriv_ut(liste):
    for i in liste:
        print(i)

# b)
def minste_av(liste):
    minste = liste[0]
    for i in liste:
        if i < minste:
            minste = i

    return i

# Oppgave 6:

# løkke 1: 1
# løkke 2: 5
