from database.connection import get_connection
from datetime import datetime


def yearly_increment():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT EMPID,SALARY,JOIN_DATE FROM EMPLOYEE")

    today = datetime.today().date()

    for empid, salary, join_date in cursor.fetchall():

        jd = datetime.strptime(join_date, "%Y-%m-%d").date()

        if (today - jd).days >= 365:

            new_salary = int(salary * 1.10)

            cursor.execute("""
            UPDATE EMPLOYEE
            SET SALARY=?
            WHERE EMPID=?
            """, (new_salary, empid))

            print("Increment applied for", empid)

    conn.commit()
    conn.close()
