#t=(1,3,4)
#print(t[2])



#x = ("apple", "banana", "cherry")
#y = list(x)
#y[1] = "kiwi"
#x = tuple(y)
 
#print(x)

''' tupveg=('peas','lemon','onion')
if 'peas' in tupveg:
	print("Yes")
else:
    print("no") '''

'''
 %writefile myfile.txt
Hello this is the text file



this is the 2nd  line '''




'''l_one=[1,2,[3,4]]
l_two=[1,2,{'k1':4}]
l_one[2][0]>=l_two[2]['k1']


#if True:
	#print('its true')

if 3>9:
	print('true')

hungry=False
if hungry:
	print('Feed me!')
else:
	print("Not hungry")'''



'''a=45
for i in range(1,10):
     print(a*i)'''


'''list=[1,2,3,4,5,6,8,33]
for li in list:
 print("li")   '''


 #Check Even no  
my_list=[1,2,3,4,5,6,8,9,0,98]
     for num in my_list:
         if num%2==0:
             print(num)

Microsoft Windows [Version 10.0.10240]
(c) 2015 Microsoft Corporation. All rights reserved.

C:\Users\pc>python
Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> True
True
>>> true
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>> pri=(22,2823,921,12,22,12)
>>> set(pri)
{921, 12, 22, 2823}
>>> list(pri)
[22, 2823, 921, 12, 22, 12]
>>> tuple(pri)
(22, 2823, 921, 12, 22, 12)
>>> dictonary(pri)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'dictonary' is not defined
>>>
>>> p=('oye','pihu','piku','piya','oye')
>>>
>>> list(p)
['oye', 'pihu', 'piku', 'piya', 'oye']
>>> set(p)
{'oye', 'piya', 'pihu', 'piku'}
>>>
>>>
>>> sort(p)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sort' is not defined
>>> sorted(p)
['oye', 'oye', 'pihu', 'piku', 'piya']
>>> p.sort()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'sort'
>>> p=['oye','pihu','piku','piya','oye']
>>>
>>> p.sort()
>>>
>>> p
['oye', 'oye', 'pihu', 'piku', 'piya']
>>>
>>> p.index(pihu)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'pihu' is not defined
>>> p.index('pihu')
2
>>> p.index('piku')
3
>>>
>>> pp=['priya','kumari','singh','rajput']
>>>
>>> pk=p+pp
>>> pk
['oye', 'oye', 'pihu', 'piku', 'piya', 'priya', 'kumari', 'singh', 'rajput']
>>> pk.index['kumari']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> pk.index('kumari')
6
>>>
>>> pp={
... name: 'piku'}
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: name 'name' is not defined
>>> pp={
... 'name':  ('piya','ziva','ziya')}
>>>
>>> pp
{'name': ('piya', 'ziva', 'ziya')}
>>> pp[name]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'name' is not defined
>>>
>>> pp['name']
('piya', 'ziva', 'ziya')
>>>
>>> pp['name'][0]
'piya'
>>> pp['name'][3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: tuple index out of range
>>>
>>> pp={'K1':{'k2':[2,3,1]}
...
... }
>>>
>>> pp
{'K1': {'k2': [2, 3, 1]}}
>>> pp['k1']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'k1'
>>> pp['K1']
{'k2': [2, 3, 1]}
>>> pp['K1'][k2][1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'k2' is not defined
>>> pp['K1']['k2'][1]
3
>>>
>>>
>>> pp={'k1':[{'k2':{'this':[2,3,4]}}]}
>>>
>>> pp['k1]
  File "<stdin>", line 1
    pp['k1]
          ^
SyntaxError: EOL while scanning string literal
>>> pp['k1']
[{'k2': {'this': [2, 3, 4]}}]
>>> pp['k1'][0]
{'k2': {'this': [2, 3, 4]}}
>>>
>>> pp['k1'][0]['k2']
{'this': [2, 3, 4]}
>>> pp['k1'][0]['k2']['this'][1]
3
>>>
>>> d={'k1':[{'nest':['this',['hello']]}]}
>>> d['k1'][0]['nest'][0][0]
't'
>>> d['k1'][0]['nest'][1][0]
'hello'
>>> d['k1']['nest'][1][0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers or slices, not str
>>>
>>> d['k1'][0]['nest'][1][0]
'hello'
>>> d['k1'][0]['nest'][2][0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>>
>>>
>>>
>>> d={'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
>>>
>>> d['k1']
[1, 2, {'k2': ['this is tricky', {'tough': [1, 2, ['hello']]}]}]
>>> d['k1'][0]['k2'][0]['tough'][0][0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not subscriptable
>>>
>>> list=[1,2,[23,233]]
>>> list[1]
2
>>> list[1][0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not subscriptable
>>> list[1][0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not subscriptable
>>>
>>> d={'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
>>>
>>> d['k1'][2]['k2'][1]['tough'][2]
['hello']
>>> d['k1'][2]['k2'][1]['tough'][2][0]
'hello'
>>>
>>>
>>> d={'k1':{'k3':[1,2,3,{'verytough':[12,33,45,[{'hey':[123,23,['hello']]}]]}]}}
>>>
>>> d['k1']['k3'][3]['verytough'][3]['hey'][2][0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers or slices, not str
>>>
>>> d['k1']['k3'][3]['verytough'][3][0]['hey'][2][0]
'hello'
>>>
>>>
>>> d={'k1':[1,2,3,4,[{'oye':[12,13,14,[{'love':[123,1234,[{'my':[19,234,'hello']}]]}]]}]]}
>>>
>>> d['k1'][4][0]['oye'][3][0]['love'][3][0]['my'][2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> d={'k1':[1,2,3,4,[{'oye':[12,13,14,[{'love':[123,1234,[{'my':[19,234,'hello']}]]}]]}]]}
>>>
>>> d['k1'][4][0]['oye'][3][0]['love'][2][0]['my'][2]
'hello'
>>>
>>>
>>> 3.0==3
True
>>> 3.0===3
  File "<stdin>", line 1
    3.0===3
         ^
SyntaxError: invalid syntax
>>>
>>> 4**2
16
>>> 4**.5
2.0
>>> 4***.5
  File "<stdin>", line 1
    4***.5
       ^
SyntaxError: invalid syntax
>>>
>>> L_one=[1,2[3,4]]
<stdin>:1: SyntaxWarning: 'int' object is not subscriptable; perhaps you missed a comma?
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not subscriptable
>>> L_one=[1,2[3,4]]
<stdin>:1: SyntaxWarning: 'int' object is not subscriptable; perhaps you missed a comma?
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not subscriptable
>>>
>>>
>>> L_one=[1,2[3,4]]
<stdin>:1: SyntaxWarning: 'int' object is not subscriptable; perhaps you missed a comma?
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not subscriptable
>>>
>>>
>>>
>>> l_one=[1,2,[3,4]]
>>> l_two=[1,2,{'k1':4}]
>>> l_one[2][0]>=l_two[2]['k1']
False
>>>
>>>
>>> l_one=[1,2,[3,4]]
>>> l_two=[1,2,{'k1':4}]
>>> l_one[2][0]==l_two[2]['k1']
False
>>> l_one[2][0]==l_two[2]['k1']
False
>>>
>>>
>>> 2==2
True
>>> 2==1
False
>>>
>>> 'Heloo'=='bye'
False
>>> 'two'=='bye'
False
>>> 'two'==='bye'
  File "<stdin>", line 1
    'two'==='bye'
           ^
SyntaxError: invalid syntax
>>>
>>>
>>> 3!=3
False
>>>
>>> 2==2 and 2==3
False
>>> 2==2 or 2==3
True
>>>
>>> 2>9
False
>>>
>>> 32<9
False
>>> 12>2
True
>>>
>>> 1<2<3
True
>>> 1<3>2
True
>>> 1<3<2
False
>>>
>>>
>>> 1==2 or 2==2
True
>>> not 1==2
True
>>>
>>> not 1==1
False
>>>
>>>
