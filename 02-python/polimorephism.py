def test(a,b):
    return  a+b
sum = test(12,34)
print(sum)
sum1 = test("navneet", "kumar")
print(sum1)
sum2 = test([1,2,3,4],[5,6,7,8])
print(sum2)

#
class data_science:

    def syllabus(self) :
        print("this is my syllabus for data science master")

class web_dev:

    def syllabus(self):
        print("this is my syllabus for web dev")

def class_person(class_obj):
    for i in class_obj :
        i.syllabus()

data_science = data_science()
web_dev = web_dev()

class_obj = [data_science , web_dev]
class_person(class_obj)
