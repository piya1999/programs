class computer:             # computer is a class
	def config(self,cpu,ram):
		self.cpu=cpu
		self.ram=ram

    def h(self):
        print("config is", self.cpu, self.ram)

com1=computer('i5',20)          #com1 & com2 are objects
com2=computer('i3',8)
#computer.config(com1)
#computer.config(com2)

com1.config()         #Also work.Normally we use this syntax