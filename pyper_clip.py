import pyperclip

# Copying a string to the clipboard
pyperclip.copy("Hello welcome to my python repository!\n I\'m using pyperclip module")

# Pasting the copied text
pasted_text = pyperclip.paste()
#printing the pasted text
print("The copied text is:",pasted_text)
