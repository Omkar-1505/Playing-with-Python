#a^2 + b^2 =c
n=int(input())
l=1
r=(n//2)
c=False
while(l<r):
    if (l**2 + r**2 == n):
        c=True
        break
    l+=1
    r-=1
if(c==True):
    print("true")
else:
    print("false")