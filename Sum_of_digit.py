def Sum_Of_Digit(num):
    sum = 0
    while num > 0:
        digit = num % 10
        sum = sum + digit
        num= num// 10
    return sum    
num = int(input("Enter a number: "))
result = Sum_Of_Digit(num)

print("Sum of digit: ",result)