#lage classe
class Motorsykkel:
#definere init med merke regnummer og km stand
    def __init__(self,merke,regnum,km):
        self.merke = merke
        self.regnum = regnum
        self.km = km
#lage metode kjør for øking av km
    def kjor(self,km):
        self.km = self.km + km
#lage metode hentkilometerstand, returner km
    def hentKilometerstand(self):
        return self.km
#lage metode skrivut, print merke, regnummer og km stand
    def skrivUt(self):
        print(self.merke)
        print(self.regnum)
        print(self.km)

