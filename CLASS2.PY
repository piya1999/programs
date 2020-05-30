class student:
 def __init__(self,name,roll):
  self.name1=name
  self.rollno=roll
  self.lap=self.laptop()

 def show(self):
  print(self.name1,self.rollno,self.lap)

 class laptop:
  def __init__(self):
   self.name='HP'
   self.ram=8

s1=student('priya',45)
s2=student('vanshi',21)
s1.show()
s2.show()