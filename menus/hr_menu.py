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
    view_pending_leaves,
    approve_leave,
    reject_leave
)

from services.payroll_service import generate_payroll

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

from models.employee_model import Employee


def hr_menu():

    while True:

        print("""
================ HR PANEL =================

--- Employee Management ---
1  Add Employee
2  Display All Employees
3  Search Employee
4  Delete Employee
5  Update Employee

--- Attendance ---
6  Mark Attendance
7  View Attendance by Employee
8  View Attendance by Date

--- Leave Management ---
9  View Pending Leaves
10 Approve Leave
11 Reject Leave

--- Payroll ---
12 Generate Payroll

--- Reports & Dashboard ---
13 Total Employees
14 Department Statistics
15 Salary Statistics

--- Export Data ---
16 Export Employees
17 Export Attendance
18 Export Leave Records

19 Logout
===========================================
""")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("\n--- Add Employee ---")
            name = input("Enter Employee Name: ")
            dept = input("Enter Department (HR / IT / Sales): ")
            mobile = int(input("Enter Mobile Number: "))
            salary = int(input("Enter Salary: "))
            emp = Employee(name, dept, mobile, salary)
            add_employee(emp)

        elif choice == "2":
            print("\n--- All Employees ---")
            display_employees()

        elif choice == "3":
            empid = int(input("Enter Employee ID: "))
            search_employee(empid)

        elif choice == "4":
            empid = int(input("Enter Employee ID to delete: "))
            delete_employee(empid)

        elif choice == "5":
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

        elif choice == "6":
            empid = int(input("Enter Employee ID: "))
            status = input("Enter Status (Present / Absent / WFH): ")
            mark_attendance(empid, status)

        elif choice == "7":
            empid = int(input("Enter Employee ID: "))
            view_attendance_by_employee(empid)

        elif choice == "8":
            date = input("Enter Date (YYYY-MM-DD): ")
            view_attendance_by_date(date)

        elif choice == "9":
            view_pending_leaves()

        elif choice == "10":
            leaveid = int(input("Enter Leave ID: "))
            approve_leave(leaveid)

        elif choice == "11":
            leaveid = int(input("Enter Leave ID: "))
            reject_leave(leaveid)

        elif choice == "12":
            empid = int(input("Enter Employee ID: "))
            bonus = int(input("Enter Bonus Amount: "))
            tax = int(input("Enter Tax Amount: "))
            generate_payroll(empid, bonus, tax)

        elif choice == "13":
            total_employees()

        elif choice == "14":
            department_statistics()

        elif choice == "15":
            salary_statistics()

        elif choice == "16":
            export_employees()

        elif choice == "17":
            export_attendance()

        elif choice == "18":
            export_leaves()

        elif choice == "19":
            print("Logging out from HR Panel...")
            break

        else:
            print("Invalid choice. Please try again.")
