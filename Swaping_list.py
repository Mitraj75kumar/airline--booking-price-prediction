# Get the number of elements from the user
n = int(input("Enter a number: "))

# Create an empty list
my_list = []

# Loop 'n' times to get elements from the user
for _ in range(n):
    num = int(input("Enter a number for the list: "))
    my_list.append(num)
print(my_list)
# Get the indices for the swap and perform the action

idx1 = int(input("Enter the first index for swapping: "))
idx2 = int(input("Enter the second index for swapping: "))

    # Perform the swap using a more concise Python method (tuple unpacking)
#my_list[idx1], my_list[idx2] = my_list[idx2], my_list[idx1]
temp= my_list[idx1]
my_list[idx1]=my_list[idx2]
my_list[idx2]= temp
print("List after swapping:", my_list)

# Handle the case where the user enters an invalid index
#except (IndexError, ValueError):
#print("Error: An invalid index or number was entered. Please check your inputs.")