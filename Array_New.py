from array import *


vals=array('i',[5,9,4,6,20])

print(vals)


for i in range(len(vals)):
    print(vals[i] , end=" ")

print("")

newArr=array(vals.typecode, (a for a in vals))

for e in newArr:
    print(e, end=" ")

print("")

#Assigning the sqaures

newArr= array(vals.typecode, (a*a for a in vals))

for e in newArr:
    print(e, end=" ")

print("")

#Same thing with while loop

i=0

while(i<len(newArr)):
    print(newArr[i], end=" ")

    i+=1

print(" ")

print("____________________________")


arr=array('i', [])

x=int(input("Enter the length of the array"))

for i in range (x):
    n=int(input("ENter the values one by one"))
    arr.append(n)

for j in range (x):
    print(arr[j], end="")




val=int(input("Enter the value for search"))

e=0
for k in arr:
    if k==val:
       print(e)
       break

    e=e+1

#Same thing using function

print(arr.index(val)) 