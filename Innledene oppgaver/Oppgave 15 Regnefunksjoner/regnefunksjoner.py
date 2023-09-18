def adisjon(tall1, tall2):
    return tall1 + tall2
def substraksjon(tall1, tall2):
    return tall1 - tall2
def divisjon(tall1, tall2):
    return tall1 / tall2
def tommerTilCm(antallTommmer):
    return antallTommmer * 2.54
#Tester
"""print(f"1+2 = {adisjon(1,2)}")
print(f"2-1 = {substraksjon(2,1)}")
print(f"25/5= {divisjon(25,5)}")
print(f"5 tommer i cm er {tommerTilCm(5)}")"""

def skrivberegninger():
    tall1 = float(input("skriv inn tall 1 "))
    tall2 = float(input("skriv inn tall 2 "))
    print(f"{tall1} / {tall2} = {divisjon(tall1,tall2)}")
    print(f"{tall1} - {tall2} = {substraksjon(tall1,tall2)}")
    print(f"{tall1} + {tall2} = {adisjon(tall1,tall2)}")

    tommer = float(input("Hvor manger tommmer "))
    print(f"{tommer} tommer er {tommerTilCm(tommer)} cm")



skrivberegninger()
