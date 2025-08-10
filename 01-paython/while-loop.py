# a = 1

# while a <= 10 :
#     print(a)
#     a = a+1

# # some of the number till some point
# n = int(input("enter your limit"))
# star_point =0
# count = 1
# while count  <= n :
#     star_point = star_point +count
#     count = count + 1
# print(star_point)

# factorial
# num = int(input("Enter number"))
# fact = 1
# while num > 0:
#     fact = fact * num
#     num  = num -1
# print(fact)

# febinaci seriese
# number = int(input("Enter the number of fab"))
# a ,b = 0,1
# counter = 0
# while counter < number :
#     print(a)
#     c = a + b
#     a = b
#     b = c
#     counter = counter + 1

# in foor
# a,b =0,1
# for i in range(10):
#     print(a)
#     c = a + b
#     a = b
#     b = c

# word = input("enter string")
# reverse = ""
# length = len(word)

# while length > 0 :
#     reverse = reverse + word[length -1]
#     length = length -1
#     print(reverse)

# table 

# n = int(input("Enter number"))
# i = 1
# while i < 11:
#     result = n*i
#     print(n,"*",i ,"=" , result)
#     i = i+1

# n = 5
# i = 1
# while i < n :
#     print(i)
#     i = i+1
# else :
#     print("this will executed once your while will complwated is sucssesfully")

# 
# comprihention

# l = [2,3,4,5,6,7,8,9]
# l1 = []
# for i in l:
#     l1.append(i**2)
# print(l1)

# print([i**2 for i in l]) # one liner work
# print([ i for i in l if i %2 ==0])   # for find even number

l1 = ["navneet","data","science"]
print([i.upper() for i in l1])

 #dict comprihention
d = {"key1" : 1 ,"ker2": 2 ,"key3":3}
print({k:v**2 for k,v in d.items()} )

print({k:v for k ,v in d.items() if v> 1})
