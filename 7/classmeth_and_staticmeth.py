class Employee:
    
    num_of_emps = 0
    raise_amt = 1.04


    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@lnup.edu.ua'
        self.pay = pay

        Employee.num_of_emps += 1
    


    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str_1.split('-')
        return cls(first, last, pay)

emp_1 = Employee('Anton', 'Pavlovskiy', 50000)
emp_2 = Employee('Test', 'User', 60000)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)



# class method
#Employee.set_raise_amt(1.05)
#print(Employee.raise_amt)
#print(emp_1.raise_amt)
#print(emp_2.raise_amt)

