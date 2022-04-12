# Escape sequences
story = "sahil is good boy.\nHe is very good"  # gives a new line
print(story)

print("tab sequence--------")
story = "sahil is good boy.\nHe\t is\t very good"  # gives a tab after He
print(story)

print("\r--------------")
story = "sahil is good boy.\nHe is ve\\ry good"
print(story)

print("backslash\\--------------")
# have to use two backslash for single backslash
story = "sahil is good\\ boy.\nHe is very good"
print(story)
