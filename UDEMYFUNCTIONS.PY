'''
def name_function():
 print("Hello")

name_function()
'''
'''
def hello(name='Name'):
 print("Hello priya!" +name)
hello("pihu")


def hello(name='Name'):
 return("Hello priya!" +name)

print(hello('piku'))


def Add_fun(num1,num2=0):
 return num1+num2

print(Add_fun(12,98))'''


#pig latin
#if word starts with a vowel,add 'ay'to the end.
#if word does not start with a vowel ,put first letter at the end and then add "ay" at last.
#word----> ordway
#apple---> appleay

def pig_Latin(letter='Fruit'):
 frst_letter=letter[0].lower()
 if frst_letter in 'aeiou':
  return letter+'ay'
 else:
  return letter[1:]+frst_letter+'ay'

print(pig_Latin('cpple'))