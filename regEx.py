# regex(regular expression) module
import re
phone_num_regex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

Match_obj=phone_num_regex.search('123-456-7890') 
# search() is a method 
#search()-it returns 'None' if the pattern does not found
#search()-it returns Match object if the pattern is found
#Match object have a group() method -it returns the actual matched object from the search string
print(" Matched phone number is found:",Match_obj.group())
