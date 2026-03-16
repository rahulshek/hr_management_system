from database.connection import get_connection
from utils.logger import log_activity


def add_employee(emp):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO EMPLOYEE
    (ENAME,DEPARTMENT,MOBILENUMBER,SALARY,JOIN_DATE)
    VALUES(?,?,?,?,?)
    """, (emp.ENAME, emp.DEPARTMENT, emp.MOBILENUMBER, emp.SALARY, emp.JOIN_DATE))

    emp.EMPID = cursor.lastrowid

    conn.commit()
    conn.close()

    log_activity(f"Employee Added: {emp.ENAME}")

    print("Employee Added:", emp.EMPID)


def display_employees():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM EMPLOYEE")

    for row in cursor.fetchall():
        print(row)

    conn.close()


def search_employee(empid):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM EMPLOYEE WHERE EMPID=?", (empid,))
    emp = cursor.fetchone()

    print(emp if emp else "Employee Not Found")

    conn.close()


def delete_employee(empid):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM EMPLOYEE WHERE EMPID=?", (empid,))

    conn.commit()
    conn.close()

    print("Employee Deleted")


def update_employee(empid, field, new_value):

    conn = get_connection()
    cursor = conn.cursor()

    query = f"UPDATE EMPLOYEE SET {field}=? WHERE EMPID=?"
    cursor.execute(query, (new_value, empid))

    conn.commit()
    conn.close()

    print("Employee Updated Successfully")
