def Fahrenheit_to_Celcius(Fahrenheit):
    Celcius = (Fahrenheit -32)*5/9
    return Celcius
Fahrenheit = float(input("Entera Fahrenheit: "))
result = Fahrenheit_to_Celcius(Fahrenheit)
print("Celcius is: ", result)