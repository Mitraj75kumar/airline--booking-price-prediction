"""
arr = [10, 20, 30, 40, 50, 60, 70 ,80, 90, 100]
print(arr)
print()
arr.append(110)
print(arr)
#arr.extend(1)
arr.insert(0, 120)
print(arr)
arr.remove(120)
print(arr)
arr.pop(-1)
print(arr)
arr.index(20)
print(arr)

#arr.clear()
arr.reverse()
print(arr)

arr.copy()
print(arr)
"""
#Reverse List 
nums = [1,2,3,4]
nums.reverse()
print(nums)

# Find largest number
List1= [10,20,90,4,60]
print("maximum number: ", max(List1))

# Count Even number

list1=[1,2,3,4,5,6,7]
count=0
for i in list1:
    if i %2==0:
        count +=1

print("Even count: ", count)

# 2nd method (List comprehension)
count1= len([num for num in nums if num%2==0])
print("Even Count", count1)

# Advanced method


count2 = len(list(filter(lambda x: x % 2 == 0, list1)))
print("Even count:", count2)
