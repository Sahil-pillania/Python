# Simple program finding Double spaces in program using find()

st = "This is a string with  double and triple   spaces"

doubleSpaces = st.find("  ")
tripleSpaces = st.find("   ")
print(doubleSpaces)  # detect double spaces into string otherwise shows -1 as output
print("And triple space: ", end="")
print(tripleSpaces)
