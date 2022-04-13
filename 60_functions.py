# Defining function
def percent(marks):          # function named percent(marks)
    p = ((marks[0] + marks[1] + marks[2] + marks[3])/400)*100
    return p


marks = [40, 89, 59, 56]
percentage1 = percent(marks)

marks2 = [81, 98, 42, 64]
percentage2 = percent(marks2)
print(percentage1, percentage2)
