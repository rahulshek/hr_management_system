from database.connection import get_connection
from datetime import date
from utils.logger import log_activity


def mark_attendance(empid, status):

    conn = get_connection()
    cursor = conn.cursor()

    today = date.today().isoformat()

    cursor.execute("""
    INSERT INTO ATTENDANCE
    (EMPID,DATE,STATUS)
    VALUES(?,?,?)
    """, (empid, today, status))

    conn.commit()
    conn.close()

    log_activity(f"Attendance Marked for EMPID {empid} : {status}")

    print("Attendance Marked")


def view_attendance_by_employee(empid):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM ATTENDANCE WHERE EMPID=?",
        (empid,)
    )

    records = cursor.fetchall()

    if records:
        for row in records:
            print(row)
    else:
        print("No attendance records found")

    conn.close()


def view_attendance_by_date(date):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM ATTENDANCE WHERE DATE=?",
        (date,)
    )

    records = cursor.fetchall()

    if records:
        for row in records:
            print(row)
    else:
        print("No records found")

    conn.close()
