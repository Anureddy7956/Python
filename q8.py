#Swapping of two variables
a=int(input("Enter the first variable (a): "))
b=int(input("Enter the second variable (b): "))
print(f"Original Values a={a},b={b}")
a=a^b
b=a^b
a=a^b
print(f"Swapped Values a={a},b={b}") 
