#1.

def adder(tall1, tall2):
    return tall1 + tall2

print("1 + 2 =", adder(1,2))
print("63 + 153 =", adder(63,153))

#2.

"""minTekst = str(input("skriv et ord "))
minBokstav = str(input("skriv en bokstav "))
count = 0
for b in ordet:
    if b == bokstav:
        count = count+1
"""
#3.
minTekst = str(input("skriv et ord "))
minBokstav = str(input("skriv en bokstav "))
def tellbokstav(ordet,bokstav):
    count = 0
    for b in ordet:
        if b == bokstav:
            count = count+1
    return count

print(f"Din bokstav kom opp {tellbokstav(minTekst,minBokstav)} ganger")

