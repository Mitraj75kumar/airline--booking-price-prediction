import numpy as np
#1Dimensional Numpy array
var = np.array([1,2,3,4,56,7])
print(var, var.ndim)
print()
print(var[4])
print("2 to 56 :",var[1:5])
print()
print("2 to 56 :",var[-5:-1])


#2Dimensional Array
var1 = np.array([[9,8,7,6],[5,4,3,2]])
print(var1)
print(var1.ndim)
print()
print("5 to 3 :",var1[1,0:3])

#3Dimensional Array
var2=np.array([[[1,2,3,4],[5,6,7,8],[11,12,13,14]]])
print(var2)
print(var2.ndim)
print()
print("11 to 14 :",var2[0,2,0:])