from array import *

a1=array('i', [1,2,3])
print (a1)



a1.append(20)
for x in a1:
    print(x)


a1.pop()
print (a1)

a1.pop(0)
print (a1)

a1.remove(2)
print (a1)

#The only difference between remove and pop is that-
#pop takes the index, and remove takes the array item itself
#Pop also returns the item which it has removed.

# LIST
#List can be a collection of heterogenous types of elements
#list is a class
#List is mutable
#List elements are indexed
#List is an iterable
#List can grow (Dynamic array)
#List can contain different type elements

#Java, C , C++ these are statically typed laguages. the type in the array acnnot be changed.
#But, On the other hand, Pyhton is Dynamically typed language. For eg. LIST


#In Pyhton, Even the array can be growable.


