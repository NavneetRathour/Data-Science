class test() :

    def test_math(self) :
        return "this is my first class"
    
class child(test) :
    pass

child_obj = child()
ch = child_obj.test_math()
print(ch)

# => multi level inheritance

class class1() :

    def test_class1(self) :
        return "this is first class"
    
class class2(class1) :

    def test_class2(self) :
        return "this is my second claas"

class class3(class2) :
    pass

obj = class3()
cl3 = obj.test_class1()
print(cl3)
cl2 = obj.test_class2()
print(cl2)

# multiple inheritance in on class

class mom():

    def love(self):
        return "mom always love his child"
    
class father():

    def cearing(self) :
        return "father having gretness of his child"

class son(mom , father) :
    pass

obj = son()
fr = obj.cearing()
lv =  obj.love()
print(lv)
print(fr)