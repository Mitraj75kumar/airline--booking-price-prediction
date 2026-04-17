def Check_Even_Odd(n):
    if n%2==0:
        return True
    else:
        return False
    
n = int(input("Enter a number is:"))
if Check_Even_Odd(n):
    print("The number is Even")
else:
    print("The number is Odd.")        
