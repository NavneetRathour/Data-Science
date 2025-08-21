l = [2,3,4,5,6]

def test(l):
    l1 = []
    for i in l :
        l1.append(i**2)
    return l1
aq = test(l)
print(aq)

# map
l2 = [2,3,4,5,6]
def sq(x):
    return x**2
sqr = list(map(sq , l))
print(sqr)

# lambda
l3 = [2,3,4,5,6]
sqi = list(map(lambda x : x**2 , l3))
print(sqi)

# sum of two list
l4 = [1,2,3,4,5]
l5 = [6,7,8,9,10]

sum = list(map(lambda x , y : x+y ,l4,l5))
print(sum)

# external function
def add(x,y) :
    return x+y
sum1= list(map(add , l4,l5))
print(sum1)

# print string to upper case help of map

s = "kanpur"
up =  list(map(lambda s: s.upper(),s) )
print(up)

# reduce function
from functools import reduce
li = [1,2,3,4,5]
sum3 = reduce(lambda x,y : x+y ,li)
print(sum3)

# find greter number
gre = reduce(lambda x,y : x if x>y else y,li)
print(gre)

# filter function
lt = [1,2,3,4,5]
even = list(filter(lambda x: x%2==0 ,lt))
print(even)
# odd
odd = list(filter(lambda x: x%2 !=0 ,lt))
print(odd)

# find negative number
lst = [-6,-7,-8,-4,6,7]
neg = list(filter(lambda x :x <0 , lst))
print(neg)

lst2 = ["navneet", "kumar","subh","ram"]
len = list(filter(lambda x : len(x)<6 , lst2))
print(len)