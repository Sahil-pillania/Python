# Program to check whether a class attribute is changed by any object from it. 
class Sample:
    a = "Harry"

obj = Sample()
obj.a = "Vikky"
# Sample.a = "Vikky"    this could change the value of a 

print(Sample.a)
print(obj.a)
# so class attribute will not be changed just a instance will be created by object.