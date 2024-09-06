class Test:
    def __init__(self):
        self.a=5
        self.b=6

t1=Test()
t2=Test()
print(t1.a, t2.b)
print(t2.a, t2.b) 


#What if you want different values?

class Test2:
    def __init__(self, i,j):
        self.a=i
        self.b=j

t1=Test2(3,4)
t2=Test2(5,6)

print(t1.a, t1.b)
print(t2.a,t2.b)

#Methods

# 1. Instance methods
class Test3:
     
     def show(self):
        self.a=3
        self.b=6
        print(self.a, self.b)

t1=Test3()
t1.show()

#2. Class method

class Test4:
         x=5
         @classmethod
         def f2(cls):
              print(cls.x)

Test4.f2()

#3. Static method

class Test5:
     
     @staticmethod
     def f3():
          print("Hello")


Test5.f3()


#init method is alos instance specific method because the argument passed is self compulsarily and it do not have any decorator above it.

        
''' 
Question:
Create a class Enmployee with attributes empid, name, salary, and also define the methods to access properties of employee.
Lesgooooooooooooooooo

'''

class Employee:
     def __init__(self, empid=None,name=None,salary=None):
          self.empid=empid
          self.name=name
          self.salary=salary


     def setEmpid(self,empid):
          self.empid=empid

     def setName(self, name):
          self.name=name
     
     def setSalary(self,salary):
          self.salary=salary

     
     def getEmpid(self):
          return self.empid
     
     def getName(self):
          return self.name
     
     def getSalary(self):
          return self.salary
     

e1=Employee()
e2=Employee(2, "Spandita",40000)
e1.setName("Vikas")
e1.setEmpid(1)
e1.setSalary(50000)

print(e1.getEmpid(), e1.getSalary(), e1.getName())
print(e2.getEmpid(), e2.getSalary(), e2.getName())

     
     
