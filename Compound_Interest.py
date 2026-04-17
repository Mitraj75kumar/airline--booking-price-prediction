def Compound_Interest( P, R, T):
    A= P * (1 + R/ 100)** T
    CI = A -P
    return CI
P = float(input("Enter a Principal Amount: "))
R = float(input("Enter a Rate: "))
T = float(input("Enter a time: "))
result= Compound_Interest(P,R, T)
print("Compound_Interest is: ", result)