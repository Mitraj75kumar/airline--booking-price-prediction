def Factorial_Number(num):
    factorial =1
    for i in range(1, num+1):

        factorial=factorial*i
    return factorial
num= int(input("Entera number: "))
result = Factorial_Number(num)
print(f"Factorial number {num} is : {result}" )    