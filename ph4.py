a=int(input("Enter 1st no"))
b=int(input("Enter 2nd no"))
c=int(input("Enter 3rd no"))
d=int(input("Enter 4th no"))
if a>b and a>c and a>d:
 print(a,"is greatest")
elif b>c and b>d:
 print(b,"is greatest")
elif c>d:
 print(c,"is greatest")
else:
 print(d,"is greatest")