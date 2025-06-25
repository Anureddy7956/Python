# D E F G H 
# D E F G H 
# D E F G H 
# D E F G H 
# D E F G H 

n= int(input("Enter the number: "))

for i in range(n):
    ch=ord('D') # ord--> Converts the character into ASCII number
    for j in range(n):
        print(chr(ch),end=" ") # chr--> converts the ASCII value back to a character 
        ch+=1
    print()