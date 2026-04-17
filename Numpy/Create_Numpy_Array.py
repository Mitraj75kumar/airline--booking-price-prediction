import numpy as np
var=np.array([1,2,3,4,5,6,7,8,9])
print(var)
n= np.arange(1,9)
print()
print(n)
print(type(n))
print(n.ndim)  #check dimension of array
var1=np.arange(1,20,5) # (start,stop,step)
print(var1)
print()
Zeros_arr=np.zeros((3,3))  # 3x3 array of zeros
Ones_arr=np.ones((2,5)) # 2x5 array of ones
full_arr=np.full((4,4),9) # 4x4 array of nines
print(Zeros_arr)
print()
print(Ones_arr)
print()
print(full_arr)
print()
identity_matrix =np.eye(3) # 3x3 identity matrix
print(identity_matrix)
# total number of element in the array
print("Total number of element in the var1 array:",var1.size)
arr= np.arange(1,11).reshape(5,2)
print()
print(arr)
matrix = np.ones((3, 3))
vector = np.array([1, 2, 3])
result = matrix + vector
print()
print(result)