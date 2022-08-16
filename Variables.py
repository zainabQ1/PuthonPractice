cars=123
_cars=45
CARS=75
name="Zainab"
company="WRP studios"

def addition ():
    a= int(input("Enter a number: "))
    b= int(input("Please enter another number: "))
    print("YOUR ANSWER IS ", a+b)

    def multiply(*args):
        product = 1
        for a in args:
            product *= a
            print("Answer: ", product)


"""
This is a printing exercise2
"""
"hi this is a comment"

print(cars)
print(_cars)
print(CARS)
print(name)

print("{} works at {}." .format(name,company))
addition()
multiply(2, 3, 45, 2)


'ARGS AND KARGS PRACTICE'



