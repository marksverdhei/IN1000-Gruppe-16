from dyr import Dyr

dyr1 = Dyr("Panda", "K", 50)
dyr2 = Dyr("Ekkorn", "M", 1)
dyr3 = Dyr("Delfin",  "K", 20)

dyrliste = [dyr1, dyr2, dyr3]

for dyr in dyrliste:
    # dyr.skriv_info()
    print("Dyr:", dyr.hent_art  (),
            " kjønn:", dyr.hent_kjonn(),
            ", og vvekt:", dyr.hent_vekt())
