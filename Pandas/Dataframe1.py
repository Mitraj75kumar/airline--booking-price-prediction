#import the pandas library to create a pandas DataFrame
import pandas as pd
# Sample Qualitative data
qualitative_data ={
    "Name":["John","Alice","Mitraj","Bob","Eve"],
    "City":["New York","Los Angles","Chicago","San Fran Cisco","Delhi"],
    "Gender":["Male","Female","Male","Female","Male"],
    "Occupation":["Engineer","Artist","Teacher","Doctor","Lawyer"],
    "Race":["Black","White","Asian","Indian","Mongolian"],
    "Smartphone Brand":["Apple","Samsung","Xiomi","Apple","Google"],


}
df=pd.DataFrame(qualitative_data)
print(df)
print()
print(df.info())
print(df.head())
print(df.describe(include="O"))

print("data frame without index")
print(df.to_string(index=False))
print(df["Name"].value_counts())
print(df["City"].value_counts())
