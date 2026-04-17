import numpy as np
var= np.array([[11,12,13,14,15,16],[1,2,3,4,5,6,]])
print(var)
print()
print(var.shape) 
print()
x=var.reshape(6,2)
print(x)
print(x.ndim)