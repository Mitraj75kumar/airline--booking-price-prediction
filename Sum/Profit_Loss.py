Cost_Price= int (input("Enter a Cost price :"))
Selling_Price= int(input("Enter aSelling price :"))
if Cost_Price > Selling_Price:
    print(f"Loss :{Cost_Price} and {Selling_Price}")
else:
    print(f"Profit :{Cost_Price} and {Selling_Price}")

Loss_amount= Cost_Price - Selling_Price
Profit_Amount = Selling_Price - Cost_Price

print(f"Loss amount : {Loss_amount}")    
print(f"Profit_amount : {Profit_Amount}")
