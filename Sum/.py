def Swap_two_numbers(a, b):
    # swap using a temporary variable
    temp = a
    a = b
    b = temp
    return a, b   # return swapped values

# Taking input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before Swapping two numbers:", (a, b))

# Call the function and update values
a, b = Swap_two_numbers(a, b)

print("After Swapping two numbers:", (a, b))
