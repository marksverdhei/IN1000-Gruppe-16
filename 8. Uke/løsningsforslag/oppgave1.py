class Sirkel:
    def __init__(self, r):
        self._radius = r

    def diameter(self):
        return self._radius * 2

    def omkrets(self):
        return self.diameter() * 3.14

    def areal(self):
        return 3.14 * (self._radius ** 2)

print(Sirkel(1).omkrets())
