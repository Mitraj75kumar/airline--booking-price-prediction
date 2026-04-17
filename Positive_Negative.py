# Check positive and negative and zero number
num = int(input("Enter a number: "))
if num>0:
    print("Positive number", num)
elif num<0:
    print("Negative number",num)
else:
    print("Zero number",num)  

def positive_negative_zero(num1):
    if num1> 0:
        return "Positive number" 
    elif num1<0:
        return "Negative number" 
    else:
        return "Zero number"


num1= int(input("Enter your number: "))
result= positive_negative_zero(num1)
print(num1, "is ", result)
       