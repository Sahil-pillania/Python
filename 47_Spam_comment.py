# Spam comment is defined as a text containing following keywords as shown in program

text = input("Enter the Text ")
if("make a lot of money fast" in text):  # usage of in 
    spam= True
elif("Buy now" in text):
    spam = True
elif("watch this" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This is spam")
else:
    print("This is not a spam")
  