"""Write a program by creating multiple function blocks to find the area of a square, rectangle,
triangle and circle, by taking the required inputs from the user."""
def square():
	side=float(input("enter the side "))
	area= side*side
	print(f"Area of the square: {area}")

def rectangle():
	length=float(input("Enter the length"))
	breadth=float(input("Enter the breadth"))
	area= length * breadth
	print(f"Area of the rectangle:{area}")

def triangle():
	base=float(input("Enter the base"))
	height=float(input("Enter the height"))
	area=0.5*base*height
	print(f"Area of triangle:{area}")
	
def circle():
	radius=float(input("Enter the radius"))
	area=3.14*radius*radius
	print(f"Area of a circle:{area}")
def main():
	while True:
		print("enter 1 to find the area of a square")
		print("enter 2 to find the area of a rectangle")
		print("enter 3 to find the area of a triangle")
		print("enter 4 to find the area of a circle")
		print("enter 5 to Exit")
		
		choice=int(input("enter the choice to find the area:"))
		if choice==1:
			square()
		elif choice==2:
			rectangle()
		elif choice==3:
			triangle()
		elif choice==4:
			circle()
		elif choice==5:
			print("Exit")
			break
main()

	
	
	
	

