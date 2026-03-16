from datetime import date


class Employee:

    def __init__(self, name, department, mobile, salary):

        self.EMPID = None
        self.ENAME = name
        self.DEPARTMENT = department
        self.MOBILENUMBER = mobile
        self.SALARY = salary
        self.JOIN_DATE = date.today().isoformat()
