
# Program using function to find greatest of three numbers
def maximum(num1, num2, num3):    # Function
    if (num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3

m = maximum(13, 55, 2)
print("The value of the maximum is " + str(m))