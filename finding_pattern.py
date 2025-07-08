#Finding Patterns of Text Without Regular Expressions
#123-456-9876
def mobile_num(text):
    if len(text)!=12:
        return False
    for i in  range(0,3):
        if  not text[i].isdecimal():
            return False
    if text[3]!='-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7]!='-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal:
            return False
    return True

user_input = input("Enter a phone number in the format XXX-XXX-XXXX: ")

if mobile_num(user_input):
    print(f"{user_input} is a ✅ valid phone number .")
else:
    print(f"{user_input} is not ❌ a valid phone number .")
