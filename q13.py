# Swapping without a temporary variable
a = int(input("Enter the variable a: "))
b = int(input("Enter the variable b: "))
print(f"Before swapping a={a},b={b}")
a, b = b, a

print(f"After swapping a={a},b={b}")

