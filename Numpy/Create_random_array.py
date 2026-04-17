import numpy as np
arr=np.random.rand(2,5) # create an array of random values
print(arr)
arr1=np.zeros((2,5))# create an array of zeros 
print(arr1)
arr2=np.ones((3,2))
print(arr2)
print(np.ones_like((arr2)))
arr4=np.full((4,5),6) # create an array of constant values
print(arr4)
print(np.full_like(arr4,7))
arr3=np.repeat((2,3),4,axis=0) #create an array in a repetitive manner
print(arr3)
print(np.tile((2),5))
# An example of repeating along x-axis
arr_1 = [[0, 1, 2], [3, 4, 5]]
print(np.repeat(arr_1, 3, axis=0))
# An example of repeating along y-axis
print(np.repeat(arr_1,3,axis=1))
#create an identy matrix
print(np.eye(3))
print(np.eye(3,k=0))
print(np.eye(4,k=1)) # An example of diagonal offset
# Create a matrix given values on the diagonal
arr = np.diag([1,2,3,4,5,6])
print(arr)
#create 0-D array with value '10'

arr=np.array(range(2,20), ndmin=3)
print(arr)
#Inspect general information of an array
print(np.info(arr))
print(arr.dtype)
arr_1=np.array(range(2,12), dtype='i4')
print(arr_1 ,"\n", arr_1.dtype)
print(arr_1.astype("U")) # Converting Data Type on Existing Arrays

