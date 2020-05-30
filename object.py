class computer:
	
	def __init__(self):            
		self.name="Navin"
		self.age=20                                                                         #ERROR -INDENTATION ERROR 

#self -reffering to object
    def update(self):
    	self.age=30

    def compare(self,c2):
        if self.age==c2.age:
            return True
        else:
            return False 

 #size of an object depends on
 #the no of variables & size of each variable
 #constructor allocates size to the obj

c1=computer()
c2=computer()
c1.name="priya"            #change name to priya
#print(id(c1))            #print address of c1
#print(id(c2))
if c1.compare(c2):
	print("They are same")

print(c1.name)
print(c2.age)
c1.update()