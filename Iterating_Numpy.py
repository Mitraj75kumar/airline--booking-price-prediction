import numpy as np
var= np.array([1,2,3,4,5,6])  # 1Dimensional array
print(var)
print()
for i in np.nditer(var): #1st method for iteration
    print(i)

print() 
for i in var:  # 2nd method for iteration
    print(i) 

#2 Dimensional Array
var1=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(var1)
print()
for i in var1:
    for j in i:
        print(j)


print() 
for i in np.nditer(var1):
    print(i)       

# 3Dimensional array
var2= np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]])
print(var2)
print()
for i in var2:
    for j in i:
        for k in j:
            print(k)


print()
for i in np.nditer(var2):
    print(i)              