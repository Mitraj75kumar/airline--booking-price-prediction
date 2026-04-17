def Simple_Interest(p, r, t):
    Simple_Interest= (p* r* t) / 100
    return Simple_Interest
p = int(input("Enter a principal amount: "))
r = int(input("Enter a rate: "))
t = int(input("Enter a time: "))
result = Simple_Interest(p, r, t)
print("Simple interest is: ", result)