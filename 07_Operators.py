# Operators in python
print("Arithmetic operators")
a = 3
b = 4

#Arithmetic operators ----
print("the value of 3+4 is ",3+4)
print("the value of 3-4 is ",3-4)
print("the value of 3/4 is ",3/4)
print("the value of 3*4 is ",3*4)

# Assignment operators----
print("Assignment operators")
a = 34    
a -=5
a /=5
a *=5
print(a)    # Here all a along with operator evaluate in sequence.

# Comparison operators
print("Comparison operators")   #returns a boolean value
b = (4>=7)
C = (4>7)
D = (4<=7)
E = (4<7)
F = (4==7)
G = (4!=7)
print(b)
print(C)
print(D)
print(E) 
print(F)
print(G)

#logical operators----
print("logical operators")
bool1 = True
bool2 = False
print("The value of bool1 and bool2 is",(bool1 and bool2))
print("The value of bool1 or bool2 is",(bool1 or bool2))
print("The value of  not bool2 is",(not bool2))