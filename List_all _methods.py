List=[11,12,13,14,15,33,22,4]
list.sort(List) # Sorts the list in place .It modifies the original list directly and returns None . You can reverse=True to sort in descending order

print(List)
List.index(12,1,6)#Returns the index of the first occurrence of the specified item. You can search within a specific slice of the list using start and end
print(List) 
item=int(input())
List.append(item) # Add an item to the end of the list
print(List.count(33)) # Returns the numbers of times an item appears in the list

m=['a','d']
List.extend(m) # Add all items from an iterable (like another list) to the end of the list
print(list.copy(List))
print(List)
print(m)
List.insert(2,88) # inserts an items specific index
print(List)
List.remove(33)#Removes the first occurence of specific item. raises a ValueError if the item isn't found
print(List)
List.pop(3)#Removes and Returns the item at the given index. If no index is specified, it removes and returns the last item
print(List)
List.clear()#Removes all items from the list, making it empty
print(List)


