unit = int(input("Enter a electric bill unit :"))

if  0 <= unit <=100:
    print("Electricity bill based on unit : ₹", unit*2)
elif 101 <= unit<200:
    print("Electricitiy bill based on unit :₹", unit *3)
elif unit>= 200:
    print("Electricity bill based on unit:₹", unit *5)
else:
    print("Invalid Unit Electricity bill")    
