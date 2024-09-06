'''
# Ways of creating arrays with NUMPY

1. array()
2. linspace()
3. logspace()
4. arrange()
5. zeros()
6. ones()


'''
from numpy import *

arr=array([1,2,3,4])
print(arr)

arr1=array([2,4,6,5.0])
print(arr1)

print(arr.dtype)
print(arr1.dtype)
print(arr.shape)

arr=linspace(0,15,16)
print(arr)

arr=linspace(0,15,20)
print(arr)


#What if we want to add 5 to each value 

arr=array([1,2,3,4,5])

arr=arr+5

print(arr)

# Adding 2 arrays

arr1= array([3,5,10])
arr2= array([32,48,90])

arr3 = arr1 + arr2

print(arr3)



