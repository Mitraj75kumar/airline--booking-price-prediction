def Check_Odd_Even(num):
    if num%2==0:
        print("Even number",num)
    else:
        print("Odd number")

    
    
    
    
num = int(input("Enter a number: "))
Check_Odd_Even(num)


# 2nd method
def Check_Even_Odd(num1):
    if num1%2==0:
        return "Even"
    else:
        return "Odd"
    
num1 = int(input("Enter a number: "))
result= Check_Even_Odd(num1)    
print(num1, "is", result)