"""num = int(input("Enter a number:"))
Square= num**2
cube= num**3
print("Number of Square:", Square)
print("Cube of number:",cube )
"""
def square_number(num):
    print("Square of this number :",num)
    result= num**2
    return result
num = int(input("Enter a number:"))
result=square_number(num)
print(f"Square of this {num} number:", result)

# Cube of number
def Cube_number(num):
    result = num**3
    return result
num= int(input("Enter a number"))
result = Cube_number(num)
print(f"Cube of number{num} is",result)