salgstall = open("salgstall.txt", "r")

def salg(filnavn):
    ordbok = {}
    liste = []
    for line in filnavn:
        liste = line.split(" ")
        ordbok[liste[0]] = int(liste[1])    
    return ordbok

ordbok = salg(salgstall)

print(ordbok)


def maanedensSalgsPerson(ordbok):
    høyest = ""
    for person in ordbok:
        if høyest == "0":
            høyest = ordbok.get(person)    
        else:    
            if ordbok.get(person) > høyest:
                høyest = ordbok.get(person)
    return høyest

def totaltAntallSalg(ordbok):
    total = 0
    for person in ordbok:
        total = total + ordbok.get(person)
    return total

def gjennomsnittSalg(ordbok):
    return totaltAntallSalg(ordbok) / len(ordbok)

print(f"Total er {totaltAntallSalg(ordbok)}")
print(f"{maanedensSalgsPerson(ordbok)}")
print(f"{gjennomsnittSalg(ordbok)}")

