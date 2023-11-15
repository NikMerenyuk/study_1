# НАСЛЕДОВАНИЕ

class Employee:

    ID = 0
    TAX = 0.13

    def __init__(self, email, salary):
        Employee.ID += 1
        self.id = Employee.ID
        self.email = email
        self.salary = salary

    def get_salary_for_month(self, bonus=0):
        return self.salary - self.salary * self.TAX + bonus

    def __str__(self):
        return f'id: {self.id}, email: {self.email}, salary: {self.salary}'


class Manager(Employee):    # Наследоваться может до трех классов
    TAX = 0.1

    def __init__(self, email, salary, employees):
        super(Manager, self).__init__(email, salary)    # Вызывает родителя нашего класса
        self.employees = employees

    def get_employees(self):
        if self.employees:
            for i_employee in self.employees:
                print(f'id: {i_employee.id}\n'
                      f'email: {i_employee.email}\n'
                      f'salary: {i_employee.salary}')

    def __str__(self):
        return f'id: {self.id}, email: {self.email}, salary: {self.salary}, employees: {self.employees}'


class Engineer(Employee):

    SAL_PER_H = 100
    TAX = 0.11

    def __init__(self, email, rank):
        super(Engineer, self).__init__(email, 0)
        self.rank = rank

    @classmethod
    def set_working_bet(cls, bet):
        cls.SAL_PER_H = bet

    def get_salary_for_month(self, bonus=0, hours=1):
        return Engineer.SAL_PER_H * hours - Engineer.SAL_PER_H * hours * self.TAX + bonus

    def __str__(self):
        return f'id: {self.id}, email: {self.email}, rank: {self.rank}'


engineer_1 = Engineer('engineer@gmail.com', '4')
# print(engineer_1)
print(engineer_1.get_salary_for_month(0, 24))

Engineer.set_working_bet(50)
print(engineer_1.get_salary_for_month(0, 24))


# employee_1 = Employee('test@gmail.com', 10000)
# # print(employee_1)
# employee_2 = Employee('test_2@gmail.com', 15000)
#
# manager_1 = Manager('boss@gmail.com', 1000000, [employee_1, employee_2])

# manager_1.get_employees()
