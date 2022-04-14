class Employee:
    company = "Google"

    def getSalary(self):
        print(
            f"Salary for this employee working in {self.company} is {self.salary}")


Sahil = Employee()
Sahil.salary = 100000
Sahil.getSalary()  # Employee.getSalary(Sahil)
