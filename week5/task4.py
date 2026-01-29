class Employee:
    def __init__(self, salary):
        self._salary = salary

    def get_salary(self):
        return self._salary

    def get_role(self):
        return "Employee"

class Manager(Employee):
    def get_role(self):
        return "Manager"

    def get_bonus(self):
        return self._salary * 0.2

def show_employees(workers):
    for w in workers:
        print(w.get_role(), w.get_salary())

e1 = Employee(200000)
e2 = Manager(300000)

show_employees([e1, e2])
