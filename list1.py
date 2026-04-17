sales_w1=[7,3,42,19,15,35,9]
sales_w2=[12,4,26,10,7,28]
sales=[]
new_days=input("Enter a lemonades for new days:")
sales_w2.append(int(new_days))
sales.extend(sales_w1)
sales.extend(sales_w2)
sales =sales_w1 + sales_w2
sales.sort()
worst_day_profit= sales[0]*1.5
best_days_profit=sales[-1]*1.5
print(f"worst days profit: ${worst_day_profit}")
print(f"Best days profit :${best_days_profit}")
print(f"Combined profit : ${worst_day_profit + best_days_profit}")