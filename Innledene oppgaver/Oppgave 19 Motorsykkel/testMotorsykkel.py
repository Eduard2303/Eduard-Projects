#import Motorsykkel classen 
from motorsykkel import Motorsykkel
#lage hovedprogramm funksjon
def hovedprogramm():
#lage 3 objekter
    mc1 = Motorsykkel("Honda","ac3091",20000)
    mc2 = Motorsykkel("BMW","ma2311",42651)
    mc3 = Motorsykkel("KTM","ba8523",25000)
#Bruke motodene
#skrive ut alle
    mc1.skrivUt()
    mc2.skrivUt()
    mc3.skrivUt()
#Øke med 10
    mc3.kjor(10)
#Skrive ut bare km
    print(mc3.hentKilometerstand())

#kalle hoved programm
hovedprogramm()
