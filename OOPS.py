# Class objects are also mutable like lists, dict.

class Customer:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def intro(self):
        print("Hi, I'm ", self.name, "and I'm", self.age, "Years Old")


c1=Customer("Nitish",34)
c2=Customer("Ankita", 32)

l=[c1,c2]

for i in l:
    i.intro()



# INHERITANCE EXAMPLE

class User:
    def login(self):
        print("login")

    def register(self):
        print("Register")


class Student(User):    # Clearly, this way of writting user in bracket is showing us that this
                        # Student class is inherited from User class. Hence, Everything fro User class can be accessed by Student class

    def enroll(self):
        print("Enroll")

    def review(self):
        print("Review")


stu1=Student()

stu1.login()
stu1.register()
stu1.enroll()
stu1.review()


