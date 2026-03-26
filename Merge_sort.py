#O(nlon(n))
def Divide(arr, l ,r):
    if(l<r):
        m = (l+r)//2
        Divide(arr, l, m)
        Divide(arr, m+1 ,r)
        merge(arr,l,m,r)  #two arrays merger

def merge(arr, l, m, r):
    #3 variables to point 3 arrays
    s1 = m-l+1
    s2 = r -(m+1)+1
    L= [0]*s1
    R=[0] *s2
    for i in range(s1):  #copying
        L[i]=arr[l+i]    #forward indexing
    for j in range(s2):
        R[j]=arr[m+1+j]
    i =j=0
    k=l
    while(i<s1 and j<s2):
        if(L[i]<R[j]):
            arr[k]=L[i]            #traversing in the original array
            i+=1
            k+=1          
        else:
            arr[k]=R[j]  
            j+=1
            k+=1
    while(i<s1):
        arr[k]=L[i]            #if anthing left
        i+=1
        k+=1 

    while(j<s2):
        arr[k]=R[j]  
        j+=1
        k+=1

arr=[21,34,56,32,43,12]
Divide(arr,0,len(arr)-1)
print(arr)