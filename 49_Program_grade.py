#Grade program 
marks = int(input("Enter your marks\n"))

if marks>90:
    grade = "A"
elif marks>80:
    grade = "B"  
elif marks>70:
    grade = "c" 
elif marks>60:
    grade = "D" 
elif marks>40:
    grade = "E" 
else:
    grade = "F"  

print("Your grade is "+grade)