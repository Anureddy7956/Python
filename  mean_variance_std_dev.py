import math
n=int(input("Enter the number length: "))
numbers=[]

for i in range(n):
    num=float(input(f"Enter the number{i+1}: "))
    numbers.append(num)

mean= sum(numbers)/n 

variance=sum((x-mean)**2 for x in numbers) # Variance: average of squared differences from the mean

std_deviation= math.sqrt(variance) #square root of variance

print(f"Mean: {mean}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_deviation}")

