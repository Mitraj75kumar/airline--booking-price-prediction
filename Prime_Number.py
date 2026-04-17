"""def Check_Prime_Number(num):
    if num <= 1:
        return "Not a Prime Number"
    for i in range(2, num):
        if num % i==0:
            return "Not a prime Number"
    return "Prime Number"

num = int(input("Enter a number: ")) 
result = Check_Prime_Number(num)
print(result)   
"""

def Print_All_Prime_Number(num):
    if num <= 1:
        return "Not a prime Number"
    for n in range(2, num + 1):
        is_prime = True
        for m in range(2, n):
            if n%m ==0:
                is_prime = False
                break
        if is_prime:
            print(n, end=" ")    
num = int(input("Enter a number : "))
Print_All_Prime_Number(num)
#print(result)      
