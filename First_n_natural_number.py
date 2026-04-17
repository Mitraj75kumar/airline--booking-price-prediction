def First_N_Natural_number(num):
    Number = []
    for i in range(1,num+1):
        if i %2!=0:
            Number.append(i)
    return Number
    
num = int(input("Enter a number: "))
#First_N_Natural_number(num)

result=First_N_Natural_number(num)  
print("First N odd number is: ", result)  