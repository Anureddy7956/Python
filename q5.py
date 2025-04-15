# Hollow square pattern
size=8
for i in range (size):  # Outer loop for rows (i = 0 to 4)
	for j in range (size):
		if i==0 or i==size-1 or j==0 or j==size-1: # Inner loop for columns (j = 0 to 4)
			print("*",end=" ")  # Print *
		else:
			print(" ", end=" ") # Print space
	print() # Moves to the next line after each row
	
	
					
		
	

