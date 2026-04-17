def Check_divisible_by_5_and_11(num):
    if num%5==0 and num%11==0:
        return "Both divisible by 5 and 11: ", num
    elif num%5==0:
        return "Disible by 5: ", num
    else:
        return "Divisible by 11: ", num
    

num = int(input("Enter a number: "))
result = Check_divisible_by_5_and_11(num)
print(result[0], result[1])    