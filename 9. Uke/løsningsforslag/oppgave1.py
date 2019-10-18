
class Person:
    def __init__(self, alder, navn):
        self._a = alder
        self._n = navn
        print(self._a, self._n)

test_person = Person(13, "Kari")
