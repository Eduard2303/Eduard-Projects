tall = 1
tallListe = []
minsum = 0
størst = 0
minst = 0

#input tall
while tall != 0:
    tall = int(input("Skriv inn tall. skriv inn 0 for å avslutte. "))
    if tall == 0:
        pass
    else:
        tallListe.append(tall)

#Skriv ut tall
for t in tallListe:
    print(t)

#finne total
for t in tallListe:
    minsum = minsum + t


#Finne minst
for t in tallListe:
    if minst == 0:
        minst = t
    else:
        if t < minst:
            minst = t
#Finne størst
for t in tallListe:
    if t > størst:
        størst = t

print(f"Det laveste tallet er {minst}")
print(f"Det høyeste tallet er {størst}")
print(f"Total summen er {minsum}")