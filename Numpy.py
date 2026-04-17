import numpy as np
from numpy import complex128
x = np.array([1,2,3,4], dtype= "c")
print("Data type :",x.dtype)
print(x)
x_2 = np.array([1,2,3,4,5,6,7])
new = x_2.astype(complex128)
print(new,  new.dtype )