a=int(input("Enter 1st no:"))
b=int(input("Enter 2nd no:"))
c=int(input("Enter 3rd no:"))
d=int(input("Enter 4th no:"))
e=int(input("Enter 5th no:"))
if a>b and a>c and a>d and a>e:
 print(a,"is greatest")
elif b>c and b>d and b>e:
 print(b,"is greatest")
elif c>d and c>e:
 print(c,"is greatest")
elif d>e:
 print(d,"is greatest")
else:
 print(e,"is greatest")