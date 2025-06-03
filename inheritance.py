# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def eat(self):
#         print("i can eat")
#     def sleep(self):
#         print("i can sleep")
# class Dog(Animal):
#     def bark(self):
#         print('i can bark')
# dog1=Dog('genera')
# dog1.eat()
# dog1.bark()
# dog1.sleep()
#
# class Name:
#     def __init__(self, name, address, age):
#         self.name = name
#         self.address = address
#         self.age = age
#
#     def details(self):
#         print("My name is " + self.name)
#
#     def addrese(self):
#         print("My address is: " + self.address)
#
#     def show_age(self):
#         print("My age is " + str(self.age))
#
# # Create object
# nnn = Name("Barsha", "Mumbai", 12)
#
# # Call methods (no parameters needed now)
# nnn.details()
# nnn.addrese()
# nnn.show_age()


# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# class Student(Person):
#     def mark(self,grade):
#         self.grade=grade
#     def details(self):
#             print("my name is"+self.name)
#             print("my age is"+str(self.age))
# stu=Student('basrsha',12)
# stu.details()

class Infor:
    def display(self):
        print('i am display')
class Finto(Infor):
    def show(self):
        print("i am a show methos")
fin=Finto()
fin.display()
fin.show()
