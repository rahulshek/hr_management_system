from services.employee_service import (
    add_employee,
    display_employees,
    search_employee,
    delete_employee,
    update_employee
)

from services.auth_service import create_user
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

from models.employee_model import Employee


def superadmin_menu():

    while True:

        print("""
================ SUPER ADMIN PANEL =================

--- User Management ---
1  Create HR User
2  Create Employee User

--- Employee Management ---
3  View All User's
4  Display All Employees
5  Search Employee
6  Delete Employee
7  Update Employee

--- Salary ---
8  Apply Yearly Increment

--- Reports & Dashboard ---
9  Total Employees
10 Department Statistics
11 Salary Statistics

--- Export Data ---
12 Export Employees
13 Export Attendance
14 Export Leave Records

15 Logout
====================================================
""")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("\n--- Create HR User ---")
            name = input("Enter Name: ")
            dept = input("Enter Department (HR / IT / Sales): ")
            mobile = int(input("Enter Mobile Number: "))
            salary = int(input("Enter Salary: "))
            emp = Employee(name, dept, mobile, salary)
            add_employee(emp)
            print(f"Employee Added with ID: {emp.EMPID}")
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            create_user(username, password, "hr", emp.EMPID)

        elif choice == "2":
            print("\n--- Create Employee User ---")
            name = input("Enter Name: ")
            dept = input("Enter Department (HR / IT / Sales): ")
            mobile = int(input("Enter Mobile Number: "))
            salary = int(input("Enter Salary: "))
            emp = Employee(name, dept, mobile, salary)
            add_employee(emp)
            print(f"Employee Added with ID: {emp.EMPID}")
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            create_user(username, password, "employee", emp.EMPID)

        elif choice == "3":
            print("\n--- All System Users ---")
            from database.connection import get_connection
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT ID, USERNAME, ROLE, EMPID FROM LOGIN")
            users = cursor.fetchall()
            if users:
                print(f"\n{'ID':<5} {'USERNAME':<15} {'ROLE':<15} {'EMPID':<10}")
                print("-" * 45)
                for u in users:
                    print(f"{u[0]:<5} {u[1]:<15} {u[2]:<15} {str(u[3]):<10}")
            else:
                print("No users found.")
            conn.close()

        elif choice == "4":
            print("\n--- All Employees ---")
            display_employees()

        elif choice == "5":
            empid = int(input("Enter Employee ID: "))
            search_employee(empid)

        elif choice == "6":
            empid = int(input("Enter Employee ID to delete: "))
            delete_employee(empid)

        elif choice == "7":
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

        elif choice == "8":
            print("\n--- Applying Yearly Increment ---")
            yearly_increment()

        elif choice == "9":
            total_employees()

        elif choice == "10":
            department_statistics()

        elif choice == "11":
            salary_statistics()

        elif choice == "12":
            export_employees()

        elif choice == "13":
            export_attendance()

        elif choice == "14":
            export_leaves()

        elif choice == "15":
            print("Logging out from Super Admin Panel...")
            break

        else:
            print("Invalid choice. Please try again.")
