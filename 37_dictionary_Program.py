# Dictionary program using hindi words and their english translation.Provide user with an option to look it up!
myDict = {
               "pankha": "fan",
               "dabba": "box",
               "vastu": "item"
}
print("options are ",myDict.keys())
a = input("Enter the hindi word: ")
#print("The meaning of your word is: ", myDict[a]) --> shows error if word not found in dictionary
print("The meaning of your word is: ", myDict.get(a))