dato1M = int(input("dato 1 måned. "))
dato1D = int(input("dato 1 dag. "))
dato2M = int(input("dato 2 måned. "))
dato2D = int(input("dato 2 dag. "))


if dato1M > dato2M:
    print("Feil rekkefølge")
elif dato2M < dato1M:
    print("Riktig rekkefølge")
elif dato1M == dato2M:
    if dato1D > dato2D:
        print("Feil rekkefølge")
    elif dato1D < dato2D:
        print("Riktig rekkefølge")
    else:
        print("Samme dato")
    