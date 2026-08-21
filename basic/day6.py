# class Class1:
#     def __init__(self,name):
#         self.name=name
#     def display(self):
#         print("my name is"+self.name)
# c1=Class1("barsha")
# c1.display()
        
# class Class1:
#     def __init__(self,name):
#         self.name=name
#     def display(self):
#         print(f"my name is {self.name}")
#     def __str__(self):
#      return self.name
# c1=Class1(12)
# c1.display()
# print(c1.name)

# class Parent:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def eat(self):
#         print("i can eat")
# class Child(Parent):
#      def sing(self):
#          print("i can sing")
# c1=Child("barsha",12)
# c1.eat()
# c1.sing()
# print(c1.name)
# print(c1.age)


class Parent:
    def __init__(self,grade):
        self.grade=grade
    def tech(self):
        print('teacher can taught')
    def stu(self):
        print(f"your garde is {self.grade}")
class Teacher(Parent):
    pass
class Student(Parent):
    pass
c1=Teacher(0)
c2=Student(12)
c1.tech()
c2.stu()