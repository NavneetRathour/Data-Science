# def fun():
#     return "navneet"     ## retun statement ko variable me store krke print krna hota h
# fun()

# def fun1():
    
#     return "navneet" ,123,[123]
# te =  fun1()
# print(te)
# def fun3(a,b):
#     s = a+b
#     print(s)

# fun3(2,3)

# def fun4():
#     a = 3+4/4
#     print(a)
# fun4()

# def fun5(n,m):
#     print(n+m)

# # fun5([1234],[5678])
# # fun5("navneet" , "kumar")

# L = [1,3,4,5, "NAVNEET" , "kumar" , [6,7,8,9]]

# l1= []
# for i in L :
#     if type(i) == int or type(i)== float :
#         l1.append(i)
# print(l1)

# def test2():
#     l1 = []
#     for i in L :
#         if type(i) == int or type(i)== float:
#             l1.append(i)
#     return l1

# sum =  test2()
# print(sum)
# t =  [1,3,4,5, "NAVNEET" , "kumar" , [6,7,8,9]]


# def test3():
#     l = []
#     for i in t:
#         if type(i)==list:
#             for j in i :
#                 l.append(j)
#     else :
#         if type(i) == int or type(i) == float :
#             l.append(i)
#     print(l)
# test3()


#  miltiple argument return

def test5(*args,a):
    return args , a
arg= test5(1,2,3 ,a= 23)
print(arg)

def test6(a,b,c=10,d=12):
    return a,b,c,d
print(test6(2,3))
print(test6(2,3,8))  # c ko override kr diya 

# key value pair 
def test7(**kwargs):
    return kwargs
dic = test7(a = [1,2,3,4],b= "navneet", c = 12.45)
print(dic)

