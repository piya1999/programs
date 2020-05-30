class car:
 wheel=4               # wheel is class variable or class namespace or static variable       Namespace=Area where u create and store object/variable
 def __init__(self):
  self.mil=10                # mil & com are instance variable or instance namespace
  self.com="BMW"

car.wheel=10
c1=car()
c2=car()
print(c1.mil,c1.com,car.wheel)
print(c2.wheel)
