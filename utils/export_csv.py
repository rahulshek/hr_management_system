import csv
from database.connection import get_connection


def export_employees():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM EMPLOYEE")

    records = cursor.fetchall()

    with open("employees.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "EMPID",
            "ENAME",
            "DEPARTMENT",
            "MOBILENUMBER",
            "SALARY",
            "JOIN_DATE"
        ])

        writer.writerows(records)

    conn.close()

    print("Employees exported to employees.csv")


def export_attendance():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM ATTENDANCE")

    records = cursor.fetchall()

    with open("attendance.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "ID",
            "EMPID",
            "DATE",
            "STATUS"
        ])

        writer.writerows(records)

    conn.close()

    print("Attendance exported to attendance.csv")


def export_leaves():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM LEAVE_REQUEST")

    records = cursor.fetchall()

    with open("leave_records.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "LEAVEID",
            "EMPID",
            "FROM_DATE",
            "TO_DATE",
            "REASON",
            "STATUS"
        ])

        writer.writerows(records)

    conn.close()

    print("Leave records exported to leave_records.csv")
