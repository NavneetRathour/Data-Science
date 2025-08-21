class test :
    pass

a = test()
print(type(a))

class pwskills :
    def welcome_massege(self):        # self for binding
        print("welcome to pwskiils")

navneet = pwskills()
print(navneet.welcome_massege()) 

ko = pwskills()
ko.welcome_massege()
print(ko)

class pwskills1 :

    def __init__(self ,phone_number , email_id ,student_id):
        self.phone_number = phone_number
        self.email_id = email_id
        self.student_id = student_id

    def return_student_deatials(self) :
        return self.student_id , self.email_id , self.phone_number

rohan = pwskills1(9696058431 , "navneet@.com", 101)
print(rohan.return_student_deatials())
print(rohan.phone_number) 
 # we create multiple object

ramji = pwskills1(457896547, "ramji.com", 108)
print(ramji.return_student_deatials())
print(ramji.email_id)

# II
class pwskills2 :

    def __init__(self ,phone_number , email_id ,student_id):
        self.phone_number1 = phone_number
        self.email_id1 = email_id
        self.student_id1 = student_id

    def return_student_deatials(self) :
        return self.student_id1 , self.email_id1 , self.phone_number1

naveen = pwskills2(15487945 , "naveen.com" , 105)
print(naveen.phone_number1)                       #=> self ke sath vala variable pta hota h
print(naveen.return_student_deatials())


# Ex= III
class pwskills3 :

    def __init__(nk ,phone_number , email_id ,student_id):
        nk.phone_number1 = phone_number
        nk.email_id1 = email_id
        nk.student_id1 = student_id

    def return_student_deatials(nk) :
        return nk.student_id1 , nk.email_id1 , nk.phone_number1

kalu = pwskills3(121131415, "kalu@.com" , 456)    
print(kalu.email_id1) 
        