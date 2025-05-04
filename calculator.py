def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Can't divide by zero"
    return x / y

def calculator():
    while True:    
        print("\nYoo!! Welcome to simple calculator")
        print("Enter number 1 for addition operation")
        print("Enter number 2 for subtraction operation")
        print("Enter number 3 for multiplication operation")
        print("Enter number 4 for division operation")
        print("Enter number 5 to EXIT")

        operation = int(input("Enter your choice (1–5): "))

        if operation == 5:
            print("Exiting calculator... Goodbye!!")
            break

        if operation in [1, 2, 3, 4]:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))

            if operation == 1:
                print("Ans:", add(x, y))
            elif operation == 2:
                print("Ans:", sub(x, y))
            elif operation == 3:
                print("Ans:", multiply(x, y))
            elif operation == 4:
                print("Ans:", divide(x, y))
        else:
            print("Invalid choice. Please select 1 to 5.")

calculator()

