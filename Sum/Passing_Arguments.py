# pass by value
def addOne(x):
    x=x+1
    print("Inside function output is :",x)

x=5
addOne(x)
print("Out side output is :",x) 

# Pass by reference
def modifyList(list):
    # list appened(4)
    list=[1,2,3,4]
    print("Inside the output",list)

list=[1,2,3] 
modifyList(list)
print("Outside the outputs is :", list)   