li = [1,2,3,"such",True,4j,345]
print(li[1])
print(li[0:2+1])
print(li[-1])
print(li[::-1])  # temprary reverse
print(li[0:7:2])
s = "python"
#print(li+s)   # not work
print(list(s))
print(li[3][2])  
print(li*2)
print(len(li))
li.append(6)   # last me add krta h
print(li)     
li.append(s)
print(li)
l = [1,2,3]
li.append(l)
print(li)
li.extend("nav")  # onley eterable data add
print(li)
l.extend([1,2,3])
print(l)
l.insert(0,"navneet")
print(l)
l.pop(1)   # delet from first index 
print(l)
l.pop()   # delet from last
print(l)
l.remove(3)  # jo value dege usi ko uda dega
l.append("kk")
print(l)
#l.reverse()   # parmanent rervers 
print(l)
l = l [::-1]    # parmanent
print(l)
l2= [2,3,8,9,6,7] 
l2.sort()           # for onley integer sorting
print(l2)
l3 = ['navneet', 'pw','kanpur','data science']
l3.sort()      # reverse=True Disending ke liye
print(l3)
l4 = ("navneet","vivek")

print(l4.index("navneet"))
print(l4.count("vivek"))

l5 = [3,5,7,8]
l5[0] = 90      # list me ye sistem chalta h
print(l5)

s = "kunal"
print(s.replace('l','k')) # one time change
print(s)   # original change nhi hogi

