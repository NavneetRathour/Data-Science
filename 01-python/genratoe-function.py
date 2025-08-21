# print(range(10))
# for i in range(10):
#     print(i)


# genrator function
# def test_fib(n):
#     a,b = 0,1
#     for i in range(n):
#         yield a            # yield for datad thorough
#         a,b = b, a+b

# for i in test_fib(10):
#     print(i)

# with while
def test_fib1():
    a,b = 0,1
    while True:
        yield a
        a,b = b ,a+b

fib = test_fib1()
for i in range(10):
    print(next(fib))
print(type(fib))

# string itrable hoti h n ki itrator
# itrator bnana padta h => macanition behind for loop

s1 ="Navneet"
print(type(s1))
s2 = iter (s1)
print(type(s2))

print(next(s2))
print(next(s2))

#Ex
def count_test(n):
    count = 1
    while count < n:
        yield count
        count = count +1

c = count_test(5)
for i in c :
    print(i)
