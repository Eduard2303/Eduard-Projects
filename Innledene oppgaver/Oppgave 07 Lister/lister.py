tall = [1, 2, 3]
total = []
tall.append(4)
#print(l[0],l[2])

for i in tall:
    total.append(i + (i+1))

for i in tall: 
    total.append(i + (i*1))

print(total)

total.pop()
total.pop()

print(total)

navn = [] 

navn.append(str(input("navn1 ")))
navn.append(str(input("navn2 ")))
navn.append(str(input("navn3 ")))
navn.append(str(input("navn4 ")))

if "Eduard" in navn or "eduard" in navn:    
    print("Du husket meg")
else:
    print("Glemte du meg?")