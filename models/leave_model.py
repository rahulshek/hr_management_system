class LeaveRequest:

    def __init__(self, empid, from_date, to_date, reason):

        self.EMPID = empid
        self.FROM_DATE = from_date
        self.TO_DATE = to_date
        self.REASON = reason
        self.STATUS = "Pending"
