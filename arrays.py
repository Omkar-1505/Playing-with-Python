#Array module

import array as arr #(alias)
import sys
val=arr.array('i',[1,2,3,4,5])  #it besically is the type code just like C's data type specification
print(val)

for i in range(len(val)):    #for loop
    print(val[i], end=" ")

for x in val: #for each loop
    print(x)

print(sys.getsizeof(val[1]))
print(val.typecode)

val.reverse()
for x in val: #for each loop
    print(x)

val.insert(2,88) #(index,value) append is also there
val[2] = 89 #over rides/replace

copyarr= arr.array(val.typecode ,(x for x in val) ) #we can also modify here by x*3
for x in copyarr: #for each loop
    print(x*3)

copyarr.pop(2) #index, if nor given then deletes the last one
copyarr.pop(3) #value

a=val[2:4] #slicing,negative indexing is also open 
b=val[::-1] #reverses everything

uarr=arr.array('i',[])   #user input
n=int(input('Enter a number'))
for i in range(n):
    uarr.append(int(input('Enter next:')))

warr=arr.array('i',[12,23,34,45,56,67])
print(warr.index(23))



#NumPy
from numpy import *

#helps to generate heterogenous array
nval=array([1,2,3,4.5,'b'],)
for x in nval:
    print(x)

tval=array([1,2,3,4.5,], int ) #helps type conversion
for x in tval:
    print(x)

#Arithmetic Progression
aval=linspace(10,20,5)  #(start,end,divisions)
a2val=arange(10,20,2)
loval=logspace(10,20,2)  #Explore more

for x in aval:
    print(x)
for x in a2val:
    print(x)
for x in loval:
    print(x)
#there are functions like zeros(no.) , ones(no./size) ,full(size,val)

#dimensional arrays
one=array([1,2,3,4,5])
two=array([[1,2,4],[5,6,7]])
print(one)
print(two)