num1 = int(input("Enter a number: "))
num2 = int(input("Enter a num 2nd:" ))
num3 = int(input("Enter a 3rd number : "))
""""
if num1>num2 and num1>num3:
    print("Maximum number is: ",num1)
elif num2>num3 and num2>num1:
    print("Maximum number is: ", num2)
else:
    print("Maximum number is: ", num3)        
"""

"""def Max_three_number(num1, num2, num3):
    if num1>num2 and num1> num3:
        return "Maximum number is : ", num1
    elif num2 >num1 and num2> num3:
        return "Maximum number is : ", num2
    else:
        return "maximum number is:  ", num3
    
num1= int(input("Enter a 1st number: "))
num2= int(input("Enter a 2nd number: "))
num3 =int(input("Enter a 3rd number: "))
result= Max_three_number(num1, num2, num3) 
print(result[0], result[1])   
"""
print("Maximum number is", max(num1, num2, num3))
print("Minimum number is: ", min(num1, num2, num3))