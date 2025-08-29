# class pwskills :

#     def student_details(self , name , email , number):
#         print(name , email , number)

# pw = pwskills()
# pw.student_details("navneet", "nk@gmail.com",9696058745)


# # => direct axex baind bhi nhi krna h like class method
# class pwskills1 :

#     def student_details(self , name , email , number):
#         print(name , email , number)

#     @staticmethod
#     def mentor_class(list_mentor):
#         print(list_mentor)

#     def mentor(self,mentor_list):
#         print(mentor_list)

# pwskills1.mentor_class(["sudh","krish"])



class pwskills2 :

    def student_details(self , name , email , number):
        print(name , email , number)

    @staticmethod
    def mentor_mail_id(mail_id_mentor):
        print(mail_id_mentor)
        

    @staticmethod
    def mentor_class(list_mentor):
        pwskills2.mentor_mail_id(["navnet@.com","shudh2.com"])
        print(list_mentor)

    @classmethod
    def class_name(cls):
        cls.mentor_class(["sudh","krish"])
    
    
    def mentor(self,mentor_list):  # => instant method
        print(mentor_list)
        self.mentor_class(["krish","sudh"]) #=> call statick method

pwskills2.mentor_class(["kresh","sudh"])
pw = pwskills2()
pw.mentor(["krish","sudh"])
