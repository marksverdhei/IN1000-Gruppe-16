class Student:
    def __init__(self, alder):
        self._alder = alder

    def hentAlder(self):
        return self._alder

studenter = {"markus" : Student(20), "julie" : Student(23),
             "sander" : Student(20), "tita" : Student(25)}

for key in studenter:
    print(key, studenter[key].hentAlder())
