# Use for ,.split,and if to create a statement that will print out words that start with 's'.
 
'''txt = "welcome to the jungle"

x = txt.split()

print(x)'''
'''
mystring="Hello everyone , my name is Priya Singh . I am a computer student .kjj srr srddfd .sfd"

words=mystring.split()
for word in words:
 if word[0].lower()=='s':
  print(word)'''
   
  # 2.Use range() to print even no.
''' 
for x in range(1,100):
 if x%2==0:
  print(x)'''


# Use a List Comprehension to create a list of all numbers
# between 1 and 50 that are divisible by 3.

#print([x for x in range (1,51) if x%3==0])


#Go Through the String below and if the length of a word is even print "even".
'''
mystring="Hloooo how are u"
for word in mystring.split():
 if len(word)%2==0:
  print(word+" is Even")
 else:
  print(word+" is Odd")
'''

 # WAP that prints the interger from 1 to 100.
 # But for multiples of three print "Fizz" instead of the
 # number, and for the multiples of five print "Buzz".
 # For numbers which are multiples of both three and five print "FizzBuzz".
'''
for num in range (1,101):
 if num%3==0 and num%5==0:
  print("fizzBuzz")
 elif num%5==0:
  print("Buzz")
 elif num%3==0:
  print("Fizz")
 else:
  print(num)
'''


#use List Comprehension to create a list of the first letter of every word in the string.

st="hloooo baby how are you!"
print([word[0] for word in st.split()])
'''for word in st.split():
 li=list(word[0])
 print(li)'''