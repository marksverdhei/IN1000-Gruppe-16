
class Person:
    def __init__(self, navn, alder):
        self._navn = navn
        self._alder = alder

    def endreNavn(self, navn):
        self._navn = navn

    def skrivNavn(self):
        print("Hei, jeg heter", self._navn)

    def skrivAlder(self):
        print("Jeg er", self._alder, "år gammel.")

person1 = Person("Magnus", 22)

person2 = Person("Nicholas", 30)

person1.skrivNavn()
person1.skrivAlder()

person2.skrivNavn()
person2.skrivAlder()
