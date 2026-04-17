def Reverse_Number(num):
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10
    return reverse

num = int(input("Enter a number: "))
result = Reverse_Number(num)

print("Reverse Number is:", result)
