#2 arrays where 1 is sorted and the other is unsorted
#key comparing
#O(n^2)
def Insertionsort(a):
    n = len(a)
    for i in range(1,n):
        key = a[i]
        j = i-1
        while(j>=0 and key <a[j]): #comparing and sorting
            a[j+1] = a[j]
            j = j-1
        a[j+1] = key

a=[64,32,25,45,40,51,2]
print(a)
Insertionsort(a)
print(a)