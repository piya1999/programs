class A:
 def feature1(self):
  print("Feature1 is displayed")
 
 def feature2(self):
  print("feature2 is displayed")

class B(A):                         #single Inheritance: Inherit class A.    class B is child class or subclass
 def feat1(self):
  print("This is feat1 in class B")

 def feat2(self):
  print("This is feat2 in class B")

class C(B):                   # Multilevel Inheritance
 def feat3(self):
   print("This is multilevel Inheritance ")

a1=B()                           #object made of class B.
a1.feature1()
a1.feature2()
a1.feat1()
a1.feat2()

c2=C()                           #object c2 access all the function of its parent and grand-parent class.This is called Multilevel inheritance.
c2.feat3()
c2.feature1()