varer = {
    "melk": 14.90,
    "brød": 24.90,
    "yoghurt": 12.90,
    "pizza": 39.90
}

print(varer)

navn1 = str(input("legg in vare navn1")) 
pris1 = int(input("legg in vare pris1"))
navn2 = str(input("legg in vare navn2")) 
pris2 = int(input("legg in vare pris2"))

varer[navn1] = pris1
varer[navn2] = pris2


print(varer)