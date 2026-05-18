#searching and placing at beginning or last
#O(n^2)
def Selectionsort(a):
    print("Filtering in Increasing Order")
    n = len(a)
    for i in range(n):
        min = i
        for j in range(i,n):
            if(a[min] > a[j]):
                min = j
        a[i],a[min] = a[min],a[i]

a=[64,32,25,45,40,51,2]
print(a)
#print(Selectionsort(a)) not work as there is no return type in that function
Selectionsort(a)
print(a)