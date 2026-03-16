from database.setup import create_tables
from models.employee_model import Employee

from services.employee_service import (
    add_employee,
    display_employees,
    search_employee,
    delete_employee,
    update_employee
)

from services.attendance_service import (
    mark_attendance,
    view_attendance_by_employee,
    view_attendance_by_date
)

from services.leave_service import (
    apply_leave,
    view_pending_leaves,
    approve_leave,
    reject_leave
)

from services.payroll_service import generate_payroll
from services.increment_service import yearly_increment

from reports.employee_reports import (
    department_statistics,
    salary_statistics,
    total_employees
)

from utils.export_csv import (
    export_employees,
    export_attendance,
    export_leaves
)

from services.auth_service import login


# ---------------- MENU ----------------
def menu():
    print("""
================ HR MANAGEMENT SYSTEM =================

1  Add Employee
2  Display Employees
3  Search Employee
4  Delete Employee
5  Mark Attendance
6  Apply Leave
7  Generate Payroll
8  Yearly Salary Increment
9  Update Employee
10 View Attendance
11 Leave Management
12 HR Dashboard
13 Export Data
14 Exit

=======================================================
""")


# ---------------- MAIN FUNCTION ----------------
def main():

    # Create database tables
    create_tables()

    # LOGIN SYSTEM
    print("\n========= HR MANAGEMENT LOGIN =========")

    username = input("Username: ")
    password = input("Password: ")

    user = login(username, password)

    if not user:
        print("Invalid login credentials")
        return

    role, empid = user
    print("\nLogin Successful\n")

    while True:

        menu()
        choice = input("Enter your choice: ").strip()

        # ADD EMPLOYEE
        if choice == "1":

            name = input("Enter Employee Name: ")
            dept = input("Enter Department (HR / IT / Sales): ")
            mobile = int(input("Enter Mobile Number: "))
            salary = int(input("Enter Salary: "))

            emp = Employee(name, dept, mobile, salary)
            add_employee(emp)

        # DISPLAY EMPLOYEES
        elif choice == "2":
            display_employees()

        # SEARCH EMPLOYEE
        elif choice == "3":
            empid = int(input("Enter Employee ID: "))
            search_employee(empid)

        # DELETE EMPLOYEE
        elif choice == "4":
            empid = int(input("Enter Employee ID to delete: "))
            delete_employee(empid)

        # MARK ATTENDANCE
        elif choice == "5":

            empid = int(input("Enter Employee ID: "))
            status = input("Enter Status (Present / Absent / WFH): ")

            mark_attendance(empid, status)

        # APPLY LEAVE
        elif choice == "6":

            empid = int(input("Enter Employee ID: "))
            from_date = input("From Date (YYYY-MM-DD): ")
            to_date = input("To Date (YYYY-MM-DD): ")
            reason = input("Reason: ")

            apply_leave(empid, from_date, to_date, reason)

        # GENERATE PAYROLL
        elif choice == "7":

            empid = int(input("Enter Employee ID: "))
            bonus = int(input("Enter Bonus Amount: "))
            tax = int(input("Enter Tax Amount: "))

            generate_payroll(empid, bonus, tax)

        # YEARLY INCREMENT
        elif choice == "8":
            yearly_increment()

        # UPDATE EMPLOYEE
        elif choice == "9":

            empid = int(input("Enter Employee ID: "))

            print("""
1 Update Name
2 Update Department
3 Update Mobile
4 Update Salary
""")

            option = input("Select field: ")

            if option == "1":
                value = input("Enter new name: ")
                update_employee(empid, "ENAME", value)

            elif option == "2":
                value = input("Enter new department: ")
                update_employee(empid, "DEPARTMENT", value)

            elif option == "3":
                value = input("Enter new mobile: ")
                update_employee(empid, "MOBILENUMBER", value)

            elif option == "4":
                value = int(input("Enter new salary: "))
                update_employee(empid, "SALARY", value)

        # VIEW ATTENDANCE
        elif choice == "10":

            print("""
1 View Attendance by Employee
2 View Attendance by Date
""")

            option = input("Enter option: ")

            if option == "1":
                empid = int(input("Enter Employee ID: "))
                view_attendance_by_employee(empid)

            elif option == "2":
                date = input("Enter Date (YYYY-MM-DD): ")
                view_attendance_by_date(date)

        # LEAVE MANAGEMENT
        elif choice == "11":

            print("""
1 View Pending Leaves
2 Approve Leave
3 Reject Leave
""")

            option = input("Enter option: ")

            if option == "1":
                view_pending_leaves()

            elif option == "2":
                leaveid = int(input("Enter Leave ID: "))
                approve_leave(leaveid)

            elif option == "3":
                leaveid = int(input("Enter Leave ID: "))
                reject_leave(leaveid)

        # HR DASHBOARD
        elif choice == "12":

            print("""
HR DASHBOARD

1 Total Employees
2 Department Statistics
3 Salary Statistics
""")

            option = input("Select option: ")

            if option == "1":
                total_employees()

            elif option == "2":
                department_statistics()

            elif option == "3":
                salary_statistics()

        # EXPORT DATA
        elif choice == "13":

            print("""
EXPORT DATA

1 Export Employees
2 Export Attendance
3 Export Leaves
""")

            option = input("Select option: ")

            if option == "1":
                export_employees()

            elif option == "2":
                export_attendance()

            elif option == "3":
                export_leaves()

        # EXIT
        elif choice == "14":
            print("Exiting HR Management System...")
            break

        else:
            print("Invalid choice. Please try again.")


# ---------------- RUN PROGRAM ----------------
if __name__ == "__main__":
    main()
