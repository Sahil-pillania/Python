# Concatination of strings
Greeting = "Good Morning, "
name = "Sahil Pillania"
print(type(name))
print(type(Greeting))
c = Greeting + name  # concatination
print(c)

# Slicing of strings
name = "Sahil"
print("value at 3rd index is: ", name[3])  # gives value at 3rd index or string
# name[3] = "d" --> does not work. We can't change index values
print(name[0:3])  # Here 3 will exclude
print(name[:4])      # is same as [0:4]
print(name[-3])      # reads value from last of string

# Skip values
name = "SahilIsIncredible"
# Here 1 shows starting, no value shows ending and final 3 shows value to be print after skipping of 2 character
d = name[1::3]
print(d)
