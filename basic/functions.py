# example 1
# def function(name):
#     print(f"hello {name}")
# function('barsha')
from _ast import arguments

# example 2
# def add(num1,num2):
#     num3=num1+num2
#     print(f"addition of two numbers is {num3}")
# add(2,3)


# lambda function
# add = lambda a,b : a+b
# print(add(1,2))

# def test(*args):
#     print(args)
# test(1,2,3)
# num1=int(input("enter the value of num1"))
# def even(num1):
#     if num1%2==0:
#         print('the number is even')
#     else:
#         print("the number is not even")
# even(num1)

# num1=int(input("enter the first one"))
# num2=int(input("enter the second number"))
# num3=int(input('enter the third number'))
# def largest(num1,num2,num3):
#     if num1>num2 and num1>num3:
#         print('num1 is grestes')
#     elif num2>num1 and num2>num3:
#         print('num2 is grestest')
#     else:
#         print("num3 is gratest")
# largest(num1,num2,num3)

# def name(name="default"):
#     print(f"my name is {name}")
# name("barsha")
# name()
    
# name=str(input('enter the name'))
# def func(name):
#     print(f"hello {name}")
# func(name)
# def func(name):
#     for  a in name:
#         print("my name is "+a)
    
# func("rahul")

# def funct(name):
#     for func in name:
#         print("name is"+func)
# name=['barhsa','rahul']   
# funct(name)

# argument pass gareko hamle yo kati wota argument pass gareko tha xaina vane
# def func(*name):
#      print("name is"+name[0] +name[1])
# func("basrha","rahul")

# keyword arguments  --- using dictionary
# def func(**name):
#      print("names are:"+name['name1'] +name['name2'])
# func(name1='barsha',name2='rahul')


# num1=int(input("enter first number"))
# num2=int(input("enter any two number"))
# def add(num1,num2):
#     num3=num1+num2
#     print(f"addition of two number is {num3}")
# add(num1,num2)


#local variable
# def name(abc):
#     print(abc)
#     a="barsha"
# name("123")

#global variable
# a='bar'

# local variable laiii global ma convert garna
# def func(abc):
#     print(abc)
#     global a
#     a="barsha"
# func("123")
# print(a)


# def func(name):
#     print("my nam eis "+name[0])
# name=['barsha','sita']
# func(name)
#
# def func(*num):
#     print(num)
# func(1,2,3)
#keyword argument
# def func(**name):
#     print("names are"+name['name1'] +name['name2'])
# func(name1="barsha",name2="sita")

# # def func(**name):
#      print("names are:"+name['name1'] +name['name2'])
# func(name1='barsha',name2='rahul')