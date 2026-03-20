from services.attendance_service import (
    mark_attendance,
    view_attendance_by_employee
)

from services.leave_service import apply_leave
from database.connection import get_connection


def view_my_profile(empid):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM EMPLOYEE WHERE EMPID=?", (empid,))
    emp = cursor.fetchone()

    if emp:
        print("\n--- My Profile ---")
        print(f"Employee ID   : {emp[0]}")
        print(f"Name          : {emp[1]}")
        print(f"Department    : {emp[2]}")
        print(f"Mobile        : {emp[3]}")
        print(f"Salary        : {emp[4]}")
        print(f"Joining Date  : {emp[5]}")
    else:
        print("Profile not found.")

    conn.close()


def view_my_leaves(empid):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM LEAVE_REQUEST WHERE EMPID=?",
        (empid,)
    )

    records = cursor.fetchall()

    if records:
        print("\n--- My Leave Requests ---")
        for row in records:
            print(
                f"LeaveID: {row[0]} | From: {row[2]} | To: {row[3]} | Reason: {row[4]} | Status: {row[5]}")
    else:
        print("No leave requests found.")

    conn.close()


def view_my_payroll(empid):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM PAYROLL WHERE EMPID=?",
        (empid,)
    )

    records = cursor.fetchall()

    if records:
        print("\n--- My Payroll Records ---")
        for row in records:
            print(
                f"ID: {row[0]} | Bonus: {row[2]} | Tax: {row[3]} | Net Salary: {row[4]}")
    else:
        print("No payroll records found.")

    conn.close()


def employee_menu(empid):

    while True:

        print(f"""
================ EMPLOYEE PANEL =================

1  View My Profile
2  Mark My Attendance
3  View My Attendance
4  Apply for Leave
5  View My Leave Status
6  View My Payroll

7  Logout
=================================================
""")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_my_profile(empid)

        elif choice == "2":
            status = input("Enter Status (Present / Absent / WFH): ")
            mark_attendance(empid, status)

        elif choice == "3":
            view_attendance_by_employee(empid)

        elif choice == "4":
            from_date = input("From Date (YYYY-MM-DD): ")
            to_date = input("To Date (YYYY-MM-DD): ")
            reason = input("Reason: ")
            apply_leave(empid, from_date, to_date, reason)

        elif choice == "5":
            view_my_leaves(empid)

        elif choice == "6":
            view_my_payroll(empid)

        elif choice == "7":
            print("Logging out from Employee Panel...")
            break

        else:
            print("Invalid choice. Please try again.")
