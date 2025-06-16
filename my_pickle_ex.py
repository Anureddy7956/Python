'''
import pickle
# Methods in pickel -dump() method and load() method 

data = {'name': 'Alice', 'age': 25}
# Open the pickled file in binary write mode
f= open('data.pickle', 'wb') # file extention is <filename.pickle>
#dump()--> Serializes the python object file and writes it to a file in the form of binary formate
f= pickle.dump(f)

# Read the pickled file in binary read mode
f= open('data.pickle', 'rb')  # rb is a read binary
#load()--> to read the pickled (serialized) object from a file 
data = pickle.load(f) 

print(data) 
'''
import pickle

data = {'name': 'Alice', 'age': 25}

# Open the file in binary write mode
f = open('data.pickle', 'wb')
pickle.dump(data, f)
f.close()

# Open the file in binary read mode
f = open('data.pickle', 'rb')
loaded_data = pickle.load(f)
f.close()

print(loaded_data)
