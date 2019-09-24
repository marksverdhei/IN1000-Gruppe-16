
svar = ""

while svar != "q":
    svar = input("Skriv inn navnet ditt: ")
    if svar.lower() == "markus":
        print("Du heter det samme som meg!")
    else:
        print("HEI,", svar.upper(), "JEG HETER MARKUS")
    # "142781".isdigit() # -> True
    # "hei".isdigit() # -> False
    # if svar.isdigit():
    #     print(svar, "* 2 =", int(svar) * 2)
    # else:
    #     print("SKRIV INN ET TALL, IKKE BOKSTAVER!!!")
