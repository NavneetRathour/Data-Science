class pwskills :

    def __init__(self ,name , email):

        self.name = name
        self.email = email

    def student_details(self):
        print(self.name , self.email)

pw = pwskills( "navneet" , "navneet2gmail.com")
print(pw.name)
print(pw.email)


class pwskills1 :

    def __init__(self ,name , email):

        self.name = name
        self.email = email

    @classmethod        #=> decoreter function    
    def details(cls , name ,email) :
            return cls(name,email)

    def student_details(self):
        print(self.name , self.email)

pw1 = pwskills1.details("sudh" , "@.com")
print(pw1.name)
print(pw1.email)


class pwskills2 :

    mobile_num = 98949591

    def __init__(self ,name , email):

        self.name = name
        self.email = email

    @classmethod                     #=> achive consept of mehted oer loding
    def change_number(cls, mobile):
         pwskills2.mobile_num = mobile    

    @classmethod        #=> decoreter function    
    def details(cls , name ,email) :
            return cls(name,email)

    def student_details(self):
        print(self.name , self.email , pwskills2.mobile_num) # over loding

pwskills2.change_number(969654)
print(pwskills2.mobile_num)
pw = pwskills2.details("navneet" , "navneet@.com")
pt = pw.student_details()


# add outsider function
class pwskills3 :

    mobile_num = 98949591

    def __init__(self ,name , email):

        self.name = name
        self.email = email

    @classmethod                     #=> achive consept of mehted oer loding
    def change_number(cls, mobile):
         pwskills2.mobile_num = mobile    

    @classmethod        #=> decoreter function    
    def details(cls , name ,email) :
            return cls(name,email)

    def student_details(self):
        print(self.name , self.email , pwskills2.mobile_num) # over loding


#outsider function
def course_details(cls, course_name) :
     print("course name is",course_name)

pwskills3.course_details = classmethod(course_details) # atach with class method
pwskills3.course_details("data science master")

# add pw3 me
def mentor(cls , list_of_mentor) :
     print(list_of_mentor)

pwskills3.mentor = classmethod(mentor)
pwskills3.mentor(["navneet", "hayder","mustapha"])



# how to deleat function
class pwskills4 :

    mobile_num = 98949591

    def __init__(self ,name , email):

        self.name = name
        self.email = email

    @classmethod                     #=> achive consept of mehted oer loding
    def change_number(cls, mobile):
         pwskills2.mobile_num = mobile    

    @classmethod        #=> decoreter function    
    def details(cls , name ,email) :
            return cls(name,email)

    def student_details(self):
        print(self.name , self.email , pwskills2.mobile_num) # over loding

del pwskills4.change_number  # change number deleat ho jayga
pwskills4.change_number(15462321)


# => deleat with deleate attribute function
delattr(pwskills4,"details")
pwskills4.details()

# => deleate function out of classmethod
delattr(pwskills4 , "student_details")  # ho gya deleat
pwskills4.student_details
# => deleat vriable
delattr(pwskills4, "  mobile_num")
pwskills4.mobile_num()

