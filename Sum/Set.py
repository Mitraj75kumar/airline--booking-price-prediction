list1=[1,2,3,4,5]
list2=[2,4,5,6,7,8]
list3=[11,2,13,4,55,66,78]
list_1=set(list1)

list_2=set(list2)

list_3=set(list3)

M=list_1.intersection(list_2)
final_set=M.intersection(list_3)
final_list=list(final_set)
print(final_list)