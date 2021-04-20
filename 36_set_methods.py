print("Method 1:")
# Creating an empty set
b = set()
print(type(b))

#Adding values to an empty set.
b.add(4) # adding value 
b.add(5) # adding value 
b.add(7) # adding value
print(b)

print("method 2:") # length of an item
print(len(b))  #print the length of set

print("method 3:")
b.remove(5) #removes 5 from set
print(b)

print("method 4:")
print(b.pop())  # removes arbitrary element from the set and return the element removed


