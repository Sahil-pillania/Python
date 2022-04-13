# Files
# reading data of file using open function
# sample.txt file will be read which is stored outside this program
f = open('sample2.txt', 'r')
# Make sure that you also have that being accessed file with this
data = f.read()
# data = f.read(5)   This will read only 5 characters in the file
print(data)
f.close()
