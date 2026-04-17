n= int(input("Enter a number:"))
for i in range(1,n+1): # loop for rows
    print(" "*(n-i), end="") #printing Spaces
# for printing digits
    for j in range(1,2*i):
        print(j, end="")

    print()    


