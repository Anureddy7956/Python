# print the frequency of each character in the string. 
str=input("enter the string: ")
freq_char={ } # Empty dictionary
for char in str:
    if char in freq_char:
        freq_char[char]+=1
    else:
        freq_char[char]=1
print("---Character Frequency---")
for char,freq in freq_char.items():
    print(f"{char},{freq}")

