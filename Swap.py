#While loop

i=0

while i<5:
    print("spandita") 
    i=i+1


#////////////////////////////////

i=5
while i>0:
    print("Diksha")
    i=i-1

    #//////////////

i=5
while i>=1:
    print("DIku")

    i=i-1


#___________________________________________

i=1


while i<5:
    print("Spandita " , end="")
    j=1
   
    
    while j<=4: 
        print("Rocks! ", end="")
        j=j+1

    i=i+1
    print()



#____________________________________________

#FOR LOOP

for i in range(11,21,1):
    print(i , end=" ")
    
print (" ")


for i in range(11,21,5):
    print(i , end=" ")

print(" ")


for i in range(20,10,-1):
    print(i, end=" ")
    
print(" ")


#________________________________________

#Break and continue




#But what if, our vending machine only have 10 candies?

'''av=5
x=int(input("How many candies do you want?"))

i=1
while i<=x:
    if i>av:
        break 

    print("CANDY")
    i+=1


print("BYE!") '''


 #Print all numbers till 100 except the once which are divisibe by 3


for i in range (1,101):
    if i%3==0 and i%5==0:
        continue

    print(i)
    i=i+1

print("Okay Bye")

       
