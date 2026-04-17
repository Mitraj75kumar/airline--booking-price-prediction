#Create DataFrame
import pandas as pd
data = {
    'Students':["Mitraj","Amit","Anamika","Shiwangi","Alka"],
    'Rank':[1,3,4,5,2],
    'Marks':[98,75,65,86,90]
}
df= pd.DataFrame(data,index=['Rows1','Rows2','Rows3','Rows4','Rows5'])
print("Student Record\n\n",df)
print()
print()
#Access a group of rows and columns in Dataframe
print("Value of Row1 :",df.loc['Rows1','Students'])
print()
#Access the group of rows and columns by integers
print("Value\n",df.iloc[[2,3,4]])