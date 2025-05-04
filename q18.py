# Checking the character is a Vowels or not a vowles
l=['a','e','i','o','u','b','x','y','r','n']
print(l[0:9])
for i in range(0,10):
	if (l[i]=='a' or l[i]=='e'or l[i]=='o'or l[i]=='u'or l[i]=='i'):
		print(f"vowels {l[i]}")
	else:
		print(f"Not a vowels {l[i]}")
	
