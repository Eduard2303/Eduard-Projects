def slaaSammen(str1,str2):
    return str1+str2

def skrivUt(liste):
    for x in liste:
        print(x)

run = True
valg = ""
str1 = ""
str2 = ""
mineord = []
while run == True:
    valg = str(input("Velg i for slå sammen u for skriv ut og s for slutte prgrammet. ")) 

    if valg == "i":
        str1 = str(input("Skriv inn det første ordet "))
        str2 = str(input("Skriv inn det andre ordet "))
        mineord.append(slaaSammen(str1,str2))
    
    elif valg == "u":
        if mineord == []:
            print("Tom liste")
        else:    
            skrivUt(mineord)
        
    elif valg == "s":
        run = False
    
    else:
        print("Ingen kommando")



