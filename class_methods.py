class Employee:
    num_of_emps = 0
    raise_amt = 1.04
    
    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        
        Employee.num_of_emps += 1
        
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):
    raise_amt = 1.10
    
    def __init__(self, first, last, pay, prog_lang) -> None:
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None) -> None:
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
            
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname())
    
emp1 = Developer("John", "Smith", 50000, "Python")
emp2 = Developer("Antony", "Jeenk", 60000, "Java")

mgr1 = Manager("Sue", "Smith", 90000, [emp1])




'''
emp_str1 = "John-Doe-70000"
emp_str2 = "Antony-Jerk-90000"
emp_str3 = "Jane-Doe-50000"

new_emp1 = Employee.from_string(emp_str1)

print(new_emp1.email)
print(new_emp1.pay)
'''
