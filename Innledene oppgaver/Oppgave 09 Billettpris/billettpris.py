def billettpris(alder,navn):
    pris = 0 
    if alder <= 17:
        pris = 30
    elif alder >= 17 and alder < 63:
        pris = 50
    else:
        pris = 35
    print(navn,"Du er", alder,"år","og din bilett koster", pris)

billettpris(15,"a")
billettpris(31,"b")
billettpris(63,"c")