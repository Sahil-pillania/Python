# String functions
story = "once upon a time there was a boy named sahil who was so mysterious"
intro = "My name is Sahil Pillania"
# Functions
print("Length of story ", end="")  # length
print(len(story))  # length function

print("Length of intro ", end="")  # length
print(len(intro))  # length function

print(story.endswith("mysterious"))  # return boolean value

print(story.count("o"))     # count the value in string gives 6
print(story.count("a"))     # count the value in string gives 6

print(story.capitalize())   # capitalize the first letter of textor string

# finds sahil with index value if not found -1 will be shown
print(story.find("sahil"))

print(story.replace("sahil", "Sahil"))  # replace all the words
