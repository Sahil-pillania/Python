# Files
 # reading data of file using open function
f = open('sample.txt', 'r')   # sample.txt file will be read which is stored outside this program
data = f.read()               # Make sure that you also have that being accessed file with this
#data = f.read(5)   This will read only 5 characters in the file
print(data)
f.close()

