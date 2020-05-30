a=int(input("Enter no:"))
b=int(input("Enter no:"))
for i in range(2,a*b):
 if i%a==0 and i%b==0:
  print(i)
  break
 
  