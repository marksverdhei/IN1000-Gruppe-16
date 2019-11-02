
tabell = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
          
def skrivRad(tabell, radnr):
    for tall in tabell[radnr]:
        print(tall, end=" ")
    print()  
    
        
def skrivKolonne(tabell, kolnr):
    for rad in tabell:
        print(rad[kolnr])


skrivRad(tabell, 0)

skrivKolonne(tabell, 1)

def prettyPrint(tabell):
    for rad in tabell:
        print(rad)
        
def prettyPrint2(tabell):
    for rad in tabell:
        for tall in rad:
            print(tall, end=" ")
        print()

def prettyPrint3(tabell):
    pass

# prettyPrint2(tabell)
skrivRad(tabell, 1)
skrivKolonne(tabell, 2)