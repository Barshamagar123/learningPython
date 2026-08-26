def square(number):
    return number*number
number=5
print(f"the square of the give number is {square(number)}")

def check_number(number):
    if number>0:
        return "positive"
    elif number<0:
        return "negative"
    else:
        return "zero"
number=0
print(f"the number is {check_number(number)}")