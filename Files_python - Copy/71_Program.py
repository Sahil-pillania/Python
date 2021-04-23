# Program to read the text from a given file "poems.txt" and find out whetheris contains the word twinkle
f = open('poems.txt')      # poems.txt file 
t = f.read()
if 'twinkle' in t:
    print("Twinkle is present")
else:
    print("Twinkle is not present")
f.close()