#String Manipulations

text=" My github repository! "
print(text.strip()) #Remove whitespaces
print(text.upper()) #Uppercase letters
print(text.lower()) #Lowercase letters 
print(text.title()) 
print(text.capitalize())
print(text.lstrip()) #left strip
print(text.rstrip()) #Right strip
print(text.find("repository"))
print(text.index("github"))
print(text.split())
print(text[8:20]) #slicing
print(text.count("t"))
print(len(text))

print("abz".isalpha()) # checking alphabets
print("1230".isdigit()) # checking digits
print("abd360".isalnum())# checking both alphabets and numbers


print("____python____".strip("_"))

a= "I love cakes!!"
print(a.replace("cakes!!","Milkshakes!!"))

a= "student@123"
print(a.startswith("stud"))
print(a.endswith("@123"))





