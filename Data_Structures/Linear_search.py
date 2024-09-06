# LINEAR SEARCH
# Time complexity: o(n) (Bigger the size of array, more the time is required)
# Also known as Brute force
# No sorting of array is required

def linear_search(arr,item):

    for i in range(len(arr)):
        if arr[i]==item:
            print(i)
    
        
    
    return -1

arr=[12,14,26,28,30,31,32]


linear_search(arr,26)


# _________________________________________________________________________________


# BINARY SEARCH
''' Clearly, Time complexity is nlogn + logn'''

def binary_search(arr,low,high,item):

    if low<=high:
        
        mid= (low+high)//2

        if arr[mid]==item:
            print(mid) 

        elif arr[mid]>item:
            return binary_search(arr,low,mid-1,item)

        else:
            return binary_search(arr,mid+1,high,item)
        




    else:
        return -1
    

arr=[12,14,26,28,30,31,32]

binary_search(arr,0,len(arr),32)





 