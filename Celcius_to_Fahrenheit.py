def Celcius_to_Fahrenheit(Celcius):
    Fahrenheit =(Celcius *(9/5)) +32
    return Fahrenheit
Celcius = int(input("Enter a celcius: "))
result = Celcius_to_Fahrenheit(Celcius) 
print("Celcius convert to Fahrenheit is: ", result)