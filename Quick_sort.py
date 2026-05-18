#O(nlon(n)) Worst Case->O(n^2)[If array already sorted]
#Divide and Conqueor
#has pivot and divide the array further and recursive way
def Quicksort(arr,l,r):
    if(l<r): #not interchange or crossing the limit
        p=partition(arr,l,r)
        Quicksort(arr,l,p-1)
        Quicksort(arr,p+1,r)

def partition(arr,l,r):
    # pivot = arr[l]
    # i = l+1
    # j = r
    # while True:
    #     while(i<j and arr[i]<pivot):
    #         i = i+1
    #     while(i<j and arr[j]>pivot):
    #         j=j-1
    #     if(i<j):
    #         arr[i],arr[j] = arr[j],arr[i]
    #     else:
    #         break
    # arr[l],arr[j] = arr[j], arr[l]    #pivot return
    # return j
    pivot = arr[r]  # Use last element as pivot
    i = l - 1
    for j in range(l, r):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]  # Place pivot in correct position
    return i + 1

arr=[21,34,54,32,56,89,32]
Quicksort(arr,0,len(arr)-1)
print(arr)

#CHECK AGAIN