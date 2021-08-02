class EmployeeFullInfo:
    def __init__(self, first_name, last_name, birthday, department, salary, position):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.department = department
        self.salary = salary
        self.position = position


class SalaryRecord:
    def __init__(self, employee_id, salary, raison):
        self.employee_id = employee_id
        self.salary = salary
        self.raison = raison


class PositionRecord:
    def __init__(self, employee_id, position):
        self.employee_id = employee_id
        self.position = position
