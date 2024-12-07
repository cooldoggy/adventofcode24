import sys
locationList = open(sys.argv[1], "r")
list1=[]
list2=[]
output = 0
for ID in locationList:
    temp = ID.split("   ")
    list1.append(int(temp[0]))
    list2.append(int(temp[1]))
list1.sort()
list2.sort()
for i in range(len(list1)):
   output += abs(list1[i] - list2[i])
print(output)
