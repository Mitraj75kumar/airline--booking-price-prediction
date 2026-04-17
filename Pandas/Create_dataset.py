import pandas as pd
data = {
    'Customer_id':['C001','C002','C003','C004','C005'],
    'Product_Category':['Electronics','Clothing','Groceries','Books','Hardware'],
    'Satisfaction_Level':['Good','Execellent','Average','Poor','Good'],
    'Item_purchased':[3,5,12,2,1],
    'Total_Spending':[405.75,320.00,180.50,45.25,120.00]
}

df=pd.DataFrame(data)
print("Online_Shopping_Record\n",df)                                                          