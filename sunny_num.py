# Sunny numbers
import math

num = int(input("Enter the number: "))
next_num = num + 1

# Calculate the square root of next_num
sqrt_next = math.sqrt(next_num)

# Check if the square root is an integer
if sqrt_next.is_integer():
    print("It is a sunny number")
else:
    print("Not a sunny number")
