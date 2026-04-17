import numpy as np
import pandas as pd
data={
    "Name":["Mitraj","Amit","Vivek"],
    "Age":[22,21,20]
}
df= pd.DataFrame(data)
Series= pd.Series(data)
print("Dataset",df)
print()
print("Series\n",Series)
#Mathematical operation
S1=pd.Series([11,12,14,13,44])
S2=pd.Series([22,23,24,25,26])
print("Addition \n", S1+ S2)
print("Multiplication\n",S1*2)
print()
print("Mean", S1.mean())
print("Min",S1.min())
print("Max", S1.max())
print("Standard Deviation",S1.std())
print()
#Boolean
print("Greater than 10 :", S1>10)
print("Even numbers :",S1[S1%2==0])
#Missing  Value check
print()
print("Is null",S1.isna())
print("Is not Null")
print(S1.notnull())
