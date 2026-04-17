import math
def Greatest_Common_Divisor(num1, num2):
    GCD= math.gcd(num1, num2)

    return GCD
num1 = int(input("Enter a 1st number : "))
num2 = int(input("Enter a 2nd number:"))
result = Greatest_Common_Divisor(num1, num2)
print("Greatest Common Divisor is : ", result)