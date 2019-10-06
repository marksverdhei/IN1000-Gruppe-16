
class Student:
    def __init__(self, navn):
        self._navn = navn

    def skriv_navn(self):
        print("Jeg heter", self._navn)

s1 = Student("Magnus")
s2 = Student("Eirik")
s3 = Student("Mia")

s1.skriv_navn()
s2.skriv_navn()
s3.skriv_navn()

studentliste = [s1, s2, s3]

for student in studentliste:
    student.skriv_navn()

# print(studentliste)
