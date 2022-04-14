class Employee:
    company = "Google"
    salary = 100


Rishi = Employee()
Sahil = Employee()

# Creating instance attribute salary for both the objects

Rishi.salary = 45
print(Rishi.salary)
print(Sahil.salary)

# Below line throws an error as address is not present in instance/class
# print(rajni.address)
