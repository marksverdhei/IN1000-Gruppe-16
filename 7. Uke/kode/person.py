
class Person:
    def __init__(self, navn, alder):
        self._navn = navn
        self._alder = alder

    def endre_navn(self, navn):
        self._navn = navn

    def skriv_navn(self):
        print("Hei, jeg heter", self._navn)

    def skriv_alder(self):
        print("Jeg er", self._alder, "år gammel.")

person1 = Person("Magnus", 22)

person2 = Person("Nicholas", 30)

person1.skriv_navn()
person1.skriv_alder()

person2.skriv_navn()
person2.skriv_alder()
