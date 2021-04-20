#Methods of dictionary
# Dictionary 
myDict =  {
    "fast": "In a quick manner",  #values with keys
    "sahil": "A Coder",            #values with keys
    "marks": [2,5,6],                 #values with keys
    1:2                                 #values with keys
}
#Methods
print("Method 1:")
print(myDict.keys())       #for keys accessing
print(type(myDict.keys()))  # type checking
print("----------------------")   # just for space
print(list(myDict.keys()))  # conversion of class dict-keys to list format

print("Method 2:")
print(list(myDict.values())) # to access values

print("Method 3:")
print(list(myDict.items())) #kind of list. Prints all contents

print("Method 4:")   # Updation of dictionary 
print(myDict)
updateDict = {
    "Rahul": "boy",
    "Shubham" : "Friend",
    "sahil": "A Dancer"  # Here value is updated from A Coder to A Dancer but not remains both in dictionary
}
myDict.update(updateDict)
print(myDict)

print("Method 5:")  # Difference between .get and [] syntax in dictionaries
print(myDict.get("sahil"))
print(myDict.get("sahil2")) #return none as sahil2 is not present in dictionary
print(myDict["harry"]) # throw error as harry not present in dictionary

