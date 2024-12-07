import sys
locationList = open(sys.argv[1], "r")
list1=[]
list2=[]
output = 0
for ID in locationList:
    temp = ID.split("   ")
    list1.append(int(temp[0]))
    list2.append(int(temp[1]))
for x in list1:
    appearances = 0
    for y in list2:
        if x == y:
            appearances += 1
    output += x*appearances
print(output)
