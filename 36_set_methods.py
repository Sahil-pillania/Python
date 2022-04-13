print("Method 1:")
# Creating an empty set
C = set()
print(type(C))

# Adding values to an empty set.
C.add(4)  # adding value
C.add(5)  # adding value
C.add(7)  # adding value
print(C)

print("method 2:")  # length of an item
print(len(C))  # print the length of set

print("method 3:")
C.remove(5)  # removes 5 from set
print(C)

print("method 4:")
print(C.pop())  # removes arbitrary element from the set and return the element removed
