#Program to compute binomialcoefficient (Given N and R).
def factorial(n):
    result=1
    for i in range(1,n+1):
        result*= i
    return result

def binomial_coefficient(n,r):
    return factorial(n)//(factorial(r)*factorial(n-r))

N=int(input("Enter N: "))
R=int(input("Enter R: "))

if R>N or R<0 or N<0:
    print("Invalid  input")
else:
    print(f"binomial coefficient of (c({N},{R})) is {binomial_coefficient(N,R)}")
