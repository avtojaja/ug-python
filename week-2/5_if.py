a = 33
b = 200
if b > a:
    print("b is greater than a")


a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")


a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")



a = 2
b = 330
# if a > b:
#     print("A")
# else:
#     print("B")
print("A") if a > b else print("B")
