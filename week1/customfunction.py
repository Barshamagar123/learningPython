def greet(name):
    return f"Hello, {name}!"
def calculate_bmi(weight,height):
    bmi=weight/(height**2)
    return round(bmi,2)


def get_status(score):
    if score>=90:
        return "excellent"
    elif score>=70:
        return "good"
    else :
        return "needs improvement"



name="BARSHA"
print(f"greeting : {greet(name)}") #function call

weight=70
height=7.2
print(f"BMI: {calculate_bmi(weight,height)}")

score=70
print(f"score you achieve is {get_status(score)}")