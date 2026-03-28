#To get universal maximum try to get local maximums to conquer

def Max_min_diff(arr):
    arr.sort()
    n = len(arr)
    mid = n//2
    max=0
    min =0
    j = n-1

    for i in range(mid):
        max = max+abs(arr[i]-arr[j])
        j-=1

        min = min+abs(arr[2*i]-arr[2*i+1])
    
    print("Max Difference=",max)
    print("Min Difference=",min)

a=[12,5,25,10,2,15,8,30]
Max_min_diff(a)


#FIND MIN. NUMBER OF DENOMINATIONS (COIN CHANGE PROBLEM)
#min no. of coins required to get 1024 value from the list of [1,2,5,10,20,50,100,500]








