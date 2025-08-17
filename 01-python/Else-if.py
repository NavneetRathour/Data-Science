# marks = int(input("enter your marks"))
# if marks >= 80:
#     print("you will be a part of A0 batch")
# elif marks >= 60 and marks < 80:
#     print("you will be a part of A1 batch")
# elif marks >= 40 and marks < 60:
#     print("you will be a part of A2 batch")
# else :
#     print("you will be a part of A3 batch")

# price = int(input("Enter price"))
# if price > 1000:
#     print("i will not purchase")
# else:
#     print("i will purchase")
   
price = int(input("Enter price"))
if price > 1000:
    print("i will not purchase")
    if price >5000:
        print("this is to much")
    elif price <2000:
        print("it's ok")
elif price <1000:
    print("i will purchase")
else :
    print("not intrested")