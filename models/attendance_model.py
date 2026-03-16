from datetime import date


class Attendance:

    def __init__(self, empid, status):

        self.EMPID = empid
        self.DATE = date.today().isoformat()
        self.STATUS = status
