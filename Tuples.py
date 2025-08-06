# t = (2,3,4,5,"nav","false",'true')
# print(type(t))
# print(len(t))
# print(t[0])
# print(t[::-1])
# print(t[0])
# t[0]=5     #=> tuple is not changebale
# print(t)
# print(t.count(5))

# print(t.index('false'))

# # list = [1,2,3,"such",True,4j,345]
# # print(list[0])
# # list[0]=9
# # print(list)


# Set
s={}
print(type(s))

s1 = {2,3,5,6,7,"work",5j+45j,}
print(type(s1))
s2 = {2,3,5,6,7,"work",5j+45j,(4,5,6)} # emutable intity set me rakh sakte like tuple
print(s2)
se = {1,1,2,3,3,4,5,6, 6,7,8,8,9}
print(se)     # set give us only unique value

li = [2,2,6,6,4,5,5,6,6,7,7]
print(li)
print(set(li))  # set function also available h

set = {12,34,45,34,46,45,57,"kunal","kk"}  # set never arenge or create assending order
print(set)
set.add(4)
print(set)
set.remove("kk")
print(set)
