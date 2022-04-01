#classes----
class Employee:
   pass
boy=Employee()
Employee2=Employee()
print(boy)
print(Employee2)


#class properties----
class Employee:
   id=None
   email=None
   first_name=None
   last_name=None
   salary=None

emp1=Employee()

emp1.id=1
emp1.email="kweeziperez@gmail.com"

emp1.specialization=None

print(emp1.id)
print(emp1.email)
print(emp1.specialization)

emp2=Employee()
emp2.nationality="Ugandan"

print(emp2.nationality) 


#the initializer function-----
class Employee:
   def __init__(self,id,age,email,first_name,last_name):
       self.id=id
       self.age=age
       self.email=email
       self.first_name=first_name
       self.last_name=last_name

       print("Object Created")

emp1=Employee(id=1,age=22,email="johnwick@company.com",
   first_name="john",
   last_name="wick"

)

emp2=Employee(id=1,age=23,email="janedoe@company.com",
   first_name="jane",
   last_name="doe"
)

print(emp1.email)
print(emp2.email)

#methods----
class Employee:
    def __init__(self,id,age,email,first_name,last_name):
        self.id=id
        self.age=age
        self.email=email
        self.first_name=first_name
        self.last_name=last_name

        print("Object Created")

    def getEmail(self):
        return self.email

    def getAge(self):
        return self.age

emp1=Employee(id=1,age=22,
    email="johnwick@company.com",
    first_name="john",
    last_name="wick"
)

emp2=Employee(id=2,age=23,
    email="janedoe@company.com",
    first_name="jane",
    last_name="doe"

)

print(emp1.getEmail())
print(emp2.getEmail())
print(emp1.getAge())
print(emp2.getAge())


#class methods----

class Employee:
    salary=200000

    @classmethod
    def getSalary(cls):
        return cls.salary

from datetime import date

class Employee:
    def __init__(self,name,age):
        self.age=age
        self.name=name

    def displayInfo(self):
        return f"name {self.name} age {self.age}"

        @classmethod
        def fromBirthYear(cls,name,birth_year):
            return cls(name=name,age=(date.today().year-birth_year))

emp1=Employee(name="john",age=24)
emp2=Employee(name="jane",birth_year=1997)

print(emp1.displayInfo())
print(emp2.displayInfo())

print(Employee.getSalary())

#static methods----
class Employee:

    age=23
    name="john"

    @staticmethod
    def bmi(height,weight):
        return (weight/(height**2))

Employee.bmi=staticmethod(Employee.bmi)

print (Employee.bmi(10,23))

#access modifiers----
class Employee:
    def __init__(self,id,age,email,salary):
        self.id=id
        self.name=name
        self.email=email
        self.salary=salary


#public method----
def displaySalary(self):
    print(f"Salary {self.salary}")

new_employee=Employee(id=1,name="Steve",email="steve@company.com",salary=200000)

print(new_employee.salary)

new_employee.displaySalary()

#inheritance----
#Employee -> Teacher

class Employee:
    def __init__(self,name,email,age):
        self.name=name
        self.email=email
        self.age=age

    def getAge(self):
        return self.age

class Teacher(Employee):
    def __init__(self,name,email,age,class_room):
        self.class_room=class_room

        Employee.__init__(self,name,email,age)

    def displayInfo(self):
        print(f"Teacher <name:{self.name} email ={self.email} age={new_teacher.getAge()} class={self.class_room}")



new_teacher=Teacher(name="wick",
    email="wick@company.com",
    age=25,
    class_room="class 5"
)
print(new_teacher.getAge())
print(new_teacher.displayInfo())






