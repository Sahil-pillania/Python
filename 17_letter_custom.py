letter = '''Dear <|Name|>,
You are selected!

Date: <|Date|>
Have a great day ahead!
'''
name = input("Enter your name\n")  # input
date = input("Enter your Date\n")  # input
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)
print(letter)
