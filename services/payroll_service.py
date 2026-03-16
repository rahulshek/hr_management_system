from database.connection import get_connection
from utils.logger import log_activity


def generate_payroll(empid, bonus, tax):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT SALARY FROM EMPLOYEE WHERE EMPID=?", (empid,))
    salary = cursor.fetchone()[0]

    net = salary + bonus - tax

    cursor.execute("""
    INSERT INTO PAYROLL
    (EMPID,BONUS,TAX,NETSALARY)
    VALUES(?,?,?,?)
    """, (empid, bonus, tax, net))

    conn.commit()
    log_activity(f"Payroll Generated for EMPID {empid}")
    conn.close()

    print("Payroll Generated:", net)
