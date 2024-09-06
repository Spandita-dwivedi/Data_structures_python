for j in range(4):
  for i in range(4):
      print("#", end="")

  print ()

print("___________")

for j in range(4):          #Rows
  for i in range(j+1):      #Columns
      print("#", end="")

  print ()


print("___________")

for j in range(4):          #Rows
  for i in range(4-j):      #Columns
      print("#", end="")

  print ()


print("___________")

#Check the prime number or not

num=int(input("Enter the number you want to check"))


for i in range(2,num):
   if num%i==0:
      print("Not prime")
      break
   
else:
   print("Prime")
      
   