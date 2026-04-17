def leap_year(year):
    if (year%4==0 and year%100!=0) or year % 400==0:
        return "Leap year: ", year
    else:
        return "Not Leap year: ",year
    
year = int(input("Enter a year: "))
result= leap_year(year)
print(result[0], result[1])    