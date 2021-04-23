# reads content from file
with open('another.txt', 'r') as f:   
     a = f.read()
print(a)

# writes content into file
with open('another.txt', 'w') as f:   
     a = f.write("Sahil")  # writes Sahil into file
print(a)  