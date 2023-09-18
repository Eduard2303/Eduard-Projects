matplan = {
    "a":["mat1","mat2","mat3"],
    "b":["mat4","mat5","mat6"],
    "c":["mat7","mat8", "mat9"]
}
for i in matplan:
    print(i)

navn = str(input("Si navn på en person. "))

if navn in matplan:
    print(matplan[navn])
else:
    print("Denne personen finnes ikke")