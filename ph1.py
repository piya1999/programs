import math
a=int(input("Enter 1st no"))
b=int(input("Enter 2nd no"))
c=int(input("Enter 3rd no"))
d=b*b-4*a*c
if d>=0:
    x=-b+math.sqrt(d)/2*a
    print("X :",x)
else:
    print("No real roots found")
