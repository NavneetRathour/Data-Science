n = 2
p = 3

def test(n,p):
    return n**p
print(test(3,2))

# lamda
l= lambda n,p : n**p
print(l(3,2))

# lambda  is one liner funcion

add = lambda x,y : x+y
print(add(2,4))

# Celcious to ferenhite

c_to_f = lambda c : (9/5)*c + 32
print(c_to_f(45))

finding_max = lambda x,y : x if x>y else y
print(finding_max(23,56))

s = "navneet"

fid_len = lambda s : len(s)
print(fid_len(s))