li = [1,2,3,"such",True,4j,345]
print(li[1])
print(li[0:2+1])
print(li[-1])
print(li[::-1])
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

