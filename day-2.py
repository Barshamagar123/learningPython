# if statement
# age=int(input("enter your age"))
# if age>18:
#     print("you are elligible for vote")
# print("you are not elligible for vote")
# if else statement
# age=int(input("enter your age"))
# if age>19:
#     print("you are elligle for vote")
# else:
#     print("you are not elligle for vote")
# handsome='True'
# good_salary='True'
# if handsome=='True' and good_salary=='True':
#     print("you can marry to a mode")
# elif handsome!='True' and good_salary=='True':
#     print("you can marry to a beutifaul girl")
# elif handsome=='True' and good_salary!='True':
#     print("you can marry with a normal girls")
# else:
#     print("you can't marry with a normal girl")
# x=int(input("enter the value of x"))
# if x==5:
#     print(" x is equal to 5")
# elif x<5:
#     print("x is less than 5")
# else:
#     print("x is greater than 5")


# conditional statement with and gates
# # age=20
# nationality="nepali"
# if age > 18 and age < 30 and nationality== "nepali":
#     print("you are elligilbe for admisision")


#conditional statement using or gates
# today='friday'
# if today=='friday' or today=='saturday':
#     print("today is  holiday")
# today=input("enter what is today")
# if today=="monday" or today=="tuesday":
#     print("today is nest day")
# else:
#     print("today is not nest day")

# conditional statement with not gate
# x=False
# if not x:
#     print("x is false")
# password=str(input("enter the password"))
# if len(password)>=8 and  password.alnum()==True:
#     print("password is correct")


direction=str(input("enter the direction is it in left side or right side"))

if direction=="left":
    print("you have at a pond")
    choose = str(input("enter do you want  to swim or wait for  boat"))
    if choose=="swim":
        print("you reached home")
        door = int(input("enter the  three door number"))
        if door == 1:
            print("door1 win")
        elif door == 2:
                print("door2 win")
        else:
            print("door3 win")
    else:
        print('sorry the boat will not arrive')

else:
     print("misson failed")
name="barsha"
print(f"my name is{name}")
print("my name is"+name)




