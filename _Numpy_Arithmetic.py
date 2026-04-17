import numpy as np

M= []
L = []
for i in range(1,6):

    var=int(input("Enter a number is "))
    #var1=int(input("Enter number is :"))
    M.append(var)
    var1=int(input("Enter number is :"))
    L.append(var1)
    var = np.array(M,ndmin=2)
    var1=np.array(L, ndmin =2)
Add=np.add(var,var1)
difference=np.subtract(var,var1)
Multiplication = np.multiply(var, var1)
division= np.divide(var,var1)
Modulus= np.mod(var, var1)
Power= np.power(var,var1)
Reciprocal= np.reciprocal(var)
print(var)
print()
print(var1)  
print()
print(f"Addition of two Numpy Array {var} and {var1} is:",Add)  
print(f"Difference of two Numpy Array {var} and {var1} is:", difference)
print(f"Multiplication of two Numpy Array {var} and {var1} is:",Multiplication)
print(f"Division of two Numpy Array {var} and {var1} is:", division)
print(f"modulus of two Numpy Array {var} and {var1} is:",Modulus)
print(f"power of two Numpy Array {var} and {var1} is:",Power)
print(f"Reciprocal of  Numpy Array {var}  is:",Reciprocal)