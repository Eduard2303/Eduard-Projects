salgstall = open("salgstall.txt", "r")

def salg(filnavn):
    ordbok = {}
    liste = []
    for line in filnavn:
        liste = line.split(" ")
        ordbok[liste[0]] = int(liste[1])    
    return ordbok

ordbok = salg(salgstall)


def maanedensSalgsPerson(ordbok):
    høyestverdi = 0
    høyestperson = ""
    for person in ordbok:
        if høyestverdi == 0:
            høyestverdi = ordbok.get(person)
            høyestperson = person    
        else:    
            if ordbok.get(person) > høyestverdi:
                høyestverdi = ordbok.get(person)
                høyestperson = person
    return høyestperson,høyestverdi

def totaltAntallSalg(ordbok):
    total = 0
    for person in ordbok:
        total = total + ordbok.get(person)
    return total

def gjennomsnittSalg(ordbok):
    return totaltAntallSalg(ordbok) / len(ordbok)

def hovedprogram(ordbok):
    print(f"Månends salgs person er {maanedensSalgsPerson(ordbok)[0]} med {maanedensSalgsPerson(ordbok)[1]} salg.")
    print(f"Aktive slegere denne måneden: {len(ordbok)} Totalt antall salg: {totaltAntallSalg(ordbok)}")
    print(f"Gjennomsnittlig salg per person er {gjennomsnittSalg(ordbok)}")

hovedprogram(ordbok)

