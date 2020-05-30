from functools import reduce
#def is_even(n):
# if n%2==0:
#     return n
num=[1,2,33,23,2]
#evens=list(filter(is_even,num))                using filter()
evens=list(filter(lambda n:n%2==0,num))          #using lambda =lambda act as a function
#using map()
doubles=list(map(lambda n:n*2,num))
double=list(map(lambda a:a*2,evens))
print(evens)
print(doubles)
print(double)

sum=reduce(lambda a,b:a+b,doubles)
print(sum)
