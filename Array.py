from array import *

a1=array('i',[1,2,3])


#for x in a1: 
   # print (x)

for i in range(3):
        print(a1[i], end='')

i=0
while (i<len(a1)):
        print (a1[i], end='')
        i=i+1
a1.append(20)  
print (a1[i], end='')
