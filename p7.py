unit=float(input("Enter unit"))
if unit<=150:
 print("Bill is :",(unit*2.40))
elif unit>150 and unit<=300:
 print("Bill is :",((150*2.40)+((unit-150)*3.00)))
else:
 print("Bill is :",((150*2.40)+((unit-300)*3.20))+((150)*3.00))

