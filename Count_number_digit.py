def Count_Digit_Number(num):
    num = abs(num)
    count= len(str(num))
    return count
num = int(input("Enter a number: "))
result= Count_Digit_Number(num)
print("Count the number of digit is: ", result)