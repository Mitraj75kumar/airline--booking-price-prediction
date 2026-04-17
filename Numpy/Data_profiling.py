import pandas as pd
data={
    "Name":["Mitraj","simran","Amit","Priya","Anjali"],
    "Age":[20,21,22,21,23],
    "Marks":[80,75,95,80,95],
    "Attendance":[90,93,85,88,94]
}
df=pd.DataFrame(data)
print(df.info())
print()
print(df.describe())
print()
print(df.isnull().sum())
print()
print(df["Age"].value_counts())
print()
print("Min Marks:",df["Marks"].min())
print()
print("Max Marks:",df["Marks"].max())