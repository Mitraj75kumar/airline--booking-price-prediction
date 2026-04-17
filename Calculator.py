Num1= int(input("Enter a Num1 :"))
Num2 = int(input("Enter a Num2 :"))
Operator = input("Enter a operator :")
match Operator:
    case'+':
     print("Addition two numbers :",Num1+Num2)
    case'-' :
      print("Substraction of two numbers:", Num1 - Num2)
    case'*' :
     print("Multiple of two numbers :", Num1 * Num2)
    case"/":
     print("Division two numbers :", Num1/Num2)
    case "%" :
     print("Remainder of two numbers :", Num1%Num2)  
   