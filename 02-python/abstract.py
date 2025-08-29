# it is a like blue print

import abc
class pwskills:
    @abc.abstractmethod
    def students_details(self):
        pass

    @abc.abstractmethod
    def student_assignment(self):
        pass

    @abc.abstractmethod
    def student_marks(self):
        pass


class student_details(pwskills):

    def students_details(self):
        return "this is the method for taking student ditails"
    
    def student_assignment(self):
        return "this is a mathod for assing details for a particular student"
    

class data_science_master(pwskills):

    def students_details(self):
        return "this will return a student details for data sience master"
    
    def student_assignment(self):
        return "this will give you a student detaild for data science"
    
    def student_marks(self):
        return "this will give us details about student marks"
    

dts = data_science_master()
mr = dts.student_marks()
print(mr)

sd = student_details()
dt = sd.students_details()
print(dt)
