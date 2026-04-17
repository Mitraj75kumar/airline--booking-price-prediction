def Table(num):
    list =[]
    for i in range(1,11):
        list.append(num*i)
        
        
    return list
num = int(input("Enter a number: "))
result = Table(num)
print("Table: ", result)    