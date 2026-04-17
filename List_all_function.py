my_list=['a','b','c','d','e']
del my_list[2] #Delete the item at index 2
print(my_list)
del my_list[1:3] # Deletes items from index 1 up to (but not including) 3
print(my_list)
print(len(my_list))#return the number of items in the list
print(max(my_list))#Return the largst item in the list
print(min(my_list))#return the smallest item in the list
#print(sum(my_list))#Returns the sum of all items in a list of numbers
print(sorted(my_list))#Returns a new ,sorted list. It doesn't change the original list