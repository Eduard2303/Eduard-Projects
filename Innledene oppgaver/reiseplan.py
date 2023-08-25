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
    i1 = int(input(f"velg liste tall mellom 0 og 2 "))
    i2 = int(input(f"velg element tall mellom 0 og 4 "))

    if 0 <= i1 <= 2 and 0 <= i2 <= 4:
        print(f"{reiseplan[i1][i2]} {i1},{i2}")
    else:
        print("Ugyldig Iutput!")


