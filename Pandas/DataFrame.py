import pandas as pd
data={
    "Id":["SO1","SO2","SO3","SO4","S05","S06"],
    "Students":["mitraj","Amit","Alka","Anamika","Shiwangi","Amisha"],
    "Rank":[101,102,103,104,105,106]
}
df=pd.DataFrame(data)
print("Student Records =\n",df)
print("Data Type\n",df.dtypes)
print("Number of Dimension :\n",df.ndim)
print("Size \n",df.size)
print("Shape :\n",df.shape)
print("Indexes",df.index)
print("\n Transpose \n",df.T)
print("First 2 rows :\n",df.head(2))
print("Last 2 rows :\n",df.tail(2))
