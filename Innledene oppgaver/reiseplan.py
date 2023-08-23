reisested = ['s0', 's1', 's2', 's3', 's4']
klesplagg = ['p0', 'p1', 'p2', 'p3', 'p4']
avreisedato = ['d0', 'd1', 'd2', 'd3', 'd4']

"""for a in range(5):
    reisested.append(str(input(f"Velg reise sted {a} ")))
    klesplagg.append(str(input(f"Velg kles plagg {a} ")))
    avreisedato.append(str(input(f"Velg avreise dato{a} ")))"""

reiseplan = [reisested,klesplagg,avreisedato]

for x in reiseplan:
    print(x)

while True:
    i1 = int(input(f"velg liste tall mellom 0 og {len(reiseplan)-1} "))
    i2 = int(input(f"velg element tall mellom 0 og {len(reiseplan[i1])-1} "))

    if i1 >=0 and i1 <= len(reiseplan-1):
        if i2 >=0 and i2 <=len(reiseplan[i1]-1):
            break
        else:
            print("Ugyldig input! i2")
    else:
        print("Ugyldig input! i1")

