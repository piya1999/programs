class A:
 def __init__(self):
 	print("IN init A")

 def feature1(self):
  print("Feature1 is displayed")
 
 def feature2(self):
  print("feature2 is displayed")

class B:                         #single Inheritance: Inherit class A.    class B is child class or subclass
 def feat1(self):
  print("This is feat1 in class B")


class C(A,B):
 def __init__(self):
 	super().__init__()                      # super is a method 
 	print("In init C")                    #MRO :Method Resolution Order (goes from left to right)


 def feat2(self):
 	print("kllslmwldm")
 def feat3(self):
 	super().feat1()          #super method is also used to call other method
  
a1=C()
a1.feat3()