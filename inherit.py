class A:
 def feature1(self):
  print("Feature1 is displayed")
 
 def feature2(self):
  print("feature2 is displayed")

class B(A):
 def feat1(self):
  print("This is feat1 in class B")

 def feat2(self):
  print("This is feat2 in class B")     

class C(B):
 def feat3(self):
  print("This is feat3 in class C")

a1=C()
a1.feature1()
a1.feature2()
a1.feat1()
a1.feat2()
a1.feat3()