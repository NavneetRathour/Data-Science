class test :

    def __init__(self, a, b):
        self.a = a
        self.b = b

t = test(12,18)
t.a = 457985
print(t.a)

# => t.a krne pr function se bahar ki value de raha h jo nhi chahiye
# => esi liye we use incapsulation
# => es ko hide krne ke liye __ ka use krege
# Ex.


class Car :
    def __init__(self , year , make , model ,speed) :

        self.__year = year
        self.__make = make
        self.__model = model
        self.__speed = speed
    
    def set_speed(self,speed) :     # => this function for speed changing
        self.__speed = 0 if speed < 0 else speed

    def get_speed(self) :  # this function for speed checking
        return self.__speed
    


c = Car(2013 , "honda" , "zx" , 0)
c.set_speed(200)
d = c.get_speed()
print(d)

class bank_acc :
    def __init__(self,balance):
        self.__balance = balance

    def diposit(self,amount):
        self.__balance = self.__balance =amount

    def withdrow(self,amount) :
        if self.__balance >=amount:
            self.__balance = self.__balance - amount
            return True
        else :
            return False
    
    def get_balance(self):
        return self.__balance

nk = bank_acc(1000)
b= nk.withdrow(500)
print(b)
nk.diposit(5000)
get= nk.get_balance()
print(get)
nk.diposit(2000)
ge=nk.get_balance()
print(ge)
we=nk.withdrow(2000)
print(we)
        

