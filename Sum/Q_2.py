Input_String=input("Enter a String :")
N= int(input("Enter a Number:"))
Alphabets="abcdefghijklmnopqrstuvwxyz"
reverse_Aplhabets =Alphabets[::-1]


dict1= dict(zip(Alphabets, reverse_Aplhabets))
prefix=Input_String[0:N-1]
suffix=Input_String[N-1:]
mirror =""
for i in range(0,len(suffix)):
     mirror=mirror + dict1[suffix[i]]
     rest= prefix + mirror
print("Final Results is :",rest)     