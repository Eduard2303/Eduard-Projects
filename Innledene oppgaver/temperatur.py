temperatur = open("temperatur.txt","r")
templiste = []
tall = 0
for line in temperatur:
    tall = float(line)
    templiste.append(round(tall))

print(templiste)

def gjenomsnitt(liste):
    return sum(liste) / len(liste)


#print(temperaturer)
print(f"Gjennom snitt er {gjenomsnitt(templiste)}")  

