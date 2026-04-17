def Palindrome_Number(num):
    temp = num
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse *10 + digit
        num = num // 10
    if temp == reverse:
        return "Palindrome Number"
    else:
        return "Not a Palindrome Number"

num = int(input("Enter a number: "))
result= Palindrome_Number(num)
print(result)        