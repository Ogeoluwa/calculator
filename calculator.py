def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

print("""Welcome to my calculator! Only four operations can be performed.
    type a for addition
        type d for division
            type m for multiplication
                type s for subtraction""")

a = int(input("Input the first number: "))
b = int(input("Input the second number: "))
ans = input("What operation do you want to perform: ").lower()

if ans == "a":
    print(f"The addition of {a} and {b} is ", addition(a,b))
elif ans == "d":
    print(f"The division of {a} and {b} is", division(a,b))
elif ans == "m":
    print(f"The multiplication of {a} and {b} is", multiplication(a,b))
elif ans == "s":
    print(f"The subtraction of {a} and {b} is", subtraction(a,b))