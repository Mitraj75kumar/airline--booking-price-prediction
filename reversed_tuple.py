input_tuple=(1,3,2,4,5,6,7)
list=[]
for x in reversed(input_tuple):
    list.append(x)

output_tuple= tuple(list) #typecasting
print(output_tuple) 
for i in input_tuple:
    print(i)