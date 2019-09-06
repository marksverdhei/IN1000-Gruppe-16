# 1: dårlige prosedyrenavn (altså lite beskrivende)
# 2: Unødvendige mellomrom mellom prosedyre og kolon
# 3: Unødvendige mellomrom i f3
# 4: f3 utfører en enkel kodelinje, så her er det ikke
#    behov for en prosedyre

def f1() :
 i = float(input("input"))
 print(i*i)

def f2() :
 i = input()
 print("velkommen til in1000 ", i)

def f3(     )    :
 print (  "Hei!"  )

f3()
f2()
f1()

# Endringer:

def gang_med_seg_selv():
 n = float(input("Skriv inn et tall så ganger jeg det med seg selv!\n>"))
 print(n * n)

def velkomst():
 svar = input()
 print("velkommen til in1000 ", i)

print("Hei")
velkomst()
gang_med_seg_selv()
