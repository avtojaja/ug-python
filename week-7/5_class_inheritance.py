# Parent class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()


# Child class of the parent class
class Student(Person):
    pass

x = Student("Mike", "Olsen")
x.printname()


# Grandchild class of the child class of the parent class
class ChildClass(Student):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = ChildClass("Mike", "Olsen", 2024)
x.welcome()
