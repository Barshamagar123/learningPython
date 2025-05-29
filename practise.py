# for x in range(1,12):
#   print(x)
# x=1
# while x<100:
#     print(x)
#     x+=1
cheese = 50
small = 150
medium = 200
large = 250

choose = input("Would you like to choose both pizza and cheese (yes/no)? ").lower()
size = input("Select the size of pizza (small/medium/large): ").lower()

if choose == "yes":
    if size == "small":
        print(f"The price of pizza and cheese is {cheese + small}")
    elif size == "medium":
        print(f"The price of pizza and cheese is {cheese + medium}")
    elif size == "large":
        print(f"The price of pizza and cheese is {cheese + large}")
    else:
        print("Invalid size selected.")
elif choose == "no":
    if size == "small":
        print(f"The price of pizza is {small}")
    elif size == "medium":
        print(f"The price of pizza is {medium}")
    elif size == "large":
        print(f"The price of pizza is {large}")
    else:
        print("Invalid size selected.")
else:
    print("Invalid choice entered.")


# homework 2
num=int(input("enter a number"))
if num%5==0:
    print(f"{num} is divisible by 5")
elif num%7==0:
    print(f"{num} is divisible by 7")
else:
    print("not divisible")


