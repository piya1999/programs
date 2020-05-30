class student:
 def __init__(self,name,roll):
  self.name1=name
  self.rollno=roll

 def show(self):
  print(self.name1,self.rollno)

s1=student('priya',45)
s2=student('vanshi',21)
s1.show()
s2.show()

#s1=student('priya',45)
#s1=student('vanshi',21)
#print(s1.name)            #output-vanshi  means call latest object



