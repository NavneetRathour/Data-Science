def Deco(func) :
    def inner_dac():
        print("start of function")
        func()
        print("end of function")
    return inner_dac
    
@Deco    
def test1() :
    print(6+9)

test1()

import time

def timer_test(func) :
    def timer_test_inner ():
        start = time.time()
        func()
        end = time.time()
        print(end - start)
    return timer_test_inner

# @Deco
# @timer_test
# def test2():
#     print(45+78)

# test2()

@timer_test
def test3():
    for i in range(100000000):
        pass

sum = test3()
print(sum)