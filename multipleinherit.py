class A:
 def feat1(self):
 	print("Hiii, I am in class A")
 def feat2(self):
 	print("hloooooo")

class B:
 def feat3(self):
 	print("This is in class B")

class C(A,B):                        #multiple Inheritance: class A and class B are inherit by class C.
 def feat4(self):
 	print("This is in class C")

c1=C()                           #object c1 can access the functions of class A and class B
c1.feat4()
c1.feat3()
c1.feat2()
c1.feat1()

b1=B()
b1.feat3()                   #object b1 cannot access the functions of class C and class A.
 		