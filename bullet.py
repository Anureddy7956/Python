#bullet marker program

def bullet_point(items):

	print("• Bullet point list: ") # Ctrl + Shift + U, then 2022 press enter -> • 
	
	for item in items:
		print(f"• {item}") 
		
def main():

	print("Enter the items for your list (enter done for finish)")
	items=[]
	
	while True:
		entry=input("Item: ")
		
		if entry=='done':
			break
		items.append(entry)
		
	bullet_point(items)
	
main()
	
