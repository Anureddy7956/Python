# sublist into a list 
def flatten(lst):
	result=[]
	for element in lst:
		if isinstance(element,list): # built in function
			result.extend(flatten(element))
		else:
			result.append(element)
	return result
nested_list=[1,[2,[3,4],5],6]
print(flatten(nested_list))

		
		
