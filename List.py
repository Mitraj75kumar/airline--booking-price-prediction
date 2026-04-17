list = ["Mitraj","Amit","Alka","Shiwangi","Anamika"]
print(list)
print("Arrange the Ascending order:",list.sort())
print(list)
print("Arrange descending order :",list.sort(reverse=True))
print(list)
new_list=[X for X in list if "a" in X] #list comprehension
print(new_list)
new_list1=[12,13,11,23,22,45,89,65,45]
List=[x for x in new_list1 if x > 20 ]
print(List)
list[1:4]=["Jaanu","ANAMIKA"]
print(list)
#Nested List use
lis1= [12,35,[11,43,77,89],34,23,44,56,78,98,90]
print(lis1[2])
M=lis1[2][3]
print(lis1)
print(M)
N= lis1.insert(2,"ANA_MITRAJ")
print(lis1)
A=lis1[3][2]="Mitrajkr"
print(lis1)