# Program to accept marks of 6 students and display them in a sorted manner.
m1 = int(input("Marks of student 1: "))  # Getting input from m1 to m6
m2 = int(input("Marks of student 2: "))
m3 = int(input("Marks of student 3: "))
m4 = int(input("Marks of student 4: "))
m5 = int(input("Marks of student 5: "))
m6 = int(input("Marks of student 6: "))

myList = [m1, m2, m3, m4, m5, m6]
myList.sort()
print(myList)
