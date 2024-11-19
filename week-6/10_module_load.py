import mymodule
mymodule.greeting("UG")
print(mymodule.person1["age"])


from mymodule import greeting as g
g("World")

from mymodule import person1 as p
print(p["country"])
