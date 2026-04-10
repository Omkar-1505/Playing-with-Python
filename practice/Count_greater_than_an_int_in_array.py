#Finding the count of numbers greater than that of a particular number in an array 
n=int(input())
l=[]
ans=[]
c=0
for i in range(n):
    k=int(input())
    l.append(k)
for i in range(len(l)):
    k=l[i]
    c=0
    for j in range(len(l)):
        p=l[j]
        if k>p:
            c+=1
    ans.append(c)
for i in range(len(ans)):
    print(ans[i])
