def introduction(first_name="Anamika", last_name="Smith"):
    print("Hello, my name is", first_name, last_name)
introduction("Mitraj")
introduction(first_name="james")
introduction()

def hi(name1, name2):
    print("Hi", name1)
    print("Hi",name2)


hi("Mitraj", "Anamika") 

def address(street, city, postal_code):
    print("Your address is:",street, "St.,", city, postal_code)

c=input("Street:")
p_c= int(input("Enter a postal_code:"))
C= input("Enter city:")

address(c,p_c,C)

def substract(a,b):
    print("Substract:",a - b)
a = int(input("Enter a 1st number:"))
b= int(input("Enter a 2nd number:"))
substract(a, b)    

