a=int(input("Enter no:"))
b=int(input("Enter no:"))
temp=1
for i in range(a-1,2,-1):
 for j in range(b-1,2):
  if a%i==0 and b%j==0:
   print(i) 
  