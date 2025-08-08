# l1 = []
# l = [1,2,3,4,4,5,6,7]
# for i in l :
#     print(i+1)  
#     l1.append(i+1)
# print(l1)

# l1 = []
# l3 = ["navneet", "zomato","momos"]
# for i in l3 :
    

#     l1.append(i.upper())
# print(l1) 
   
# l = [1,2,3,4,5,"kumar","jam",234,456,"vinod"]
# l1_num = []
# l2_str = []
# for i in l:
#     if type(i) == int or type (i) == float:
#         l1_num.append(i)
#     else :
#         l2_str.append(i)

# print(l1_num)
# print(l2_str)

# l = [1,2,3,4,5]
# for i in l :
#     print(i,type(i))

# # for else
# for i in l :
#     print(i)
# else :
#     print("if for loop is able to compleate it selfe then onley else will exicuet ")

# l1 = ["navneet", "kumar","Rathour"]

# for i in l1 :
#     if i== "kumar":
#         break
#     print(i)

# l1 = ["navneet", "kumar","Rathour"]

# for i in l1 :
#     if i == 'kumar':
#         break
#     print(i)
# else :
#     print("execue this if for loop is able to compleate itelfe")

# for i in l1 :
#     if i == "kumar" :
#         continue
#     print(i)
# else :
#     print("execue this if for loop is able to compleate itelfe")

print( list(range(0,5)))
print( list(range(0,20,2)))
print( list(range(-10,2)))

l1 = ["navneet", "kumar","Rathour"]
for i in range(len(l1)):
    print(l1[i])

for i  in range(len(l1)-1,-1,-1):  # negetive ke liye
    print(l1[i])

l2 = [12,34,56,76,767,89,90,34,56,45,67,88]
for i in range(0,len(l2),2):
    print(l2[i])

l3 = [23,45,6,7,898,99,]
#print(sum(l3))
result  = 0
for i in l3 :
    result = result+i
print(result)


tup = (1,2,3,4,5,6)
for i in tup:
    print(i)

set = {1,2,3,4,"kumar","mohit"}
for i in set:
    print(i)

str = "Navneet"
for i in str :
    print(i)

dict = {"name": "navneet","class": "data science master", "topic":["python","states","matching","DL","CV","NLP","resume","interview"]}
print(dict)
for i in dict.keys():
    print(dict[i])
for i in dict.items():
    print(i)