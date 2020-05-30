#mylist=[1,2,3]

#for num in range(0,10,3):
	#print(num)

#print(list(range(0,12,4)))

'''index=0
for letter in 'ABCDEFGH':
 #print('letter at {} is letter{}'.format(index,letter))
 print(f"letter at index {index} is {letter}") 
 index+=1'''

'''#index=0
for word in enumerate('Priya Rajput'):
	print(word)
                               #enumerate function return the value with index position.


mylist=[1,2,3,4,5]
list2=['priya','pihu','hbjhj']
for item in zip(mylist,list2):
 print(item)
'''


'''from random import shuffle
mylist=[1,3,4,6,7,8,2]
shuffle(mylist)
print(mylist)'''

'''from random import randint
lis=randint(0,42)
print(lis)'''

'''res=input("Enter no")
print(res)  

mylist=[1,2,3,4,56,42]
for digit in mylist:
 print(digit)
 #mylist.append("piya")
 #print(list(mylist))


mylist=['y']
for let in mylist:
  mylist.append('pp')
  print(mylist)           #['y']
  print(let)              #y
  '''
'''
mystring=["hello",'pihu','ziya']
mylist=[]
for letter in mystring:
 mylist.append(letter)
 print(list(letter))

mystring='piku'
mylist=[letter for letter in mystring]
print(mystring)'''

#my=[p**3 for p in range (1,24)]
#print(my)

#li=[let for  let in range(0,101,2)]
#print(li)

#print([let for let in range(0,100)])

#print([x for x in range(0,100) if x%5!=0 and x%2!=0])

#print([x for x in range (1,200,3)])
'''
celcius to fahrenheit
celcius=[10,20,34.5,98.4,50]
print([((9/5)*t+32) for t in celcius])'''
'''
fahren=[]
celcius=[10,20,34.5,98.4,50]
for temp in celcius:
 fahren.append( ((9/5)*temp+32) )
print(fahren)
'''

mylist=[]

'''for x in range(0,6):
 for y in range(100,106):
  mylist.append(x*y)
print(list(mylist))'''

'''
import time 
for x in [2,4,8]:
 for y in [100,200,300,400]:
  mylist.append(x*y)
  time.sleep(1)
  print(mylist)
'''


