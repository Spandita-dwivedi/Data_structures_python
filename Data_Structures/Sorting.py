# BUBBLE SORT
# time complexity is n^2




def Bubble_sort (arr):

    for i in range (len(arr)-1):
        for j in range (len(arr)-1 -i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    print(arr)

arr=[12,15,1,90,45]
Bubble_sort(arr)