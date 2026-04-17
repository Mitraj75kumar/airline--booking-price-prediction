import math
def LCM_Of_Two_Number(num1, num2):
    LCM= math.lcm(num1, num2)
    return LCM
num1 = int(input("Enter a 1st number: "))
num2 = int(input("Enter a2nd number:"))
result= LCM_Of_Two_Number(num1, num2)
print("LCM of two number is: ", result)