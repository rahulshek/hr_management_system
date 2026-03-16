from database.connection import get_connection


def department_statistics():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT DEPARTMENT, COUNT(*)
    FROM EMPLOYEE
    GROUP BY DEPARTMENT
    """)

    records = cursor.fetchall()

    print("\nDepartment Statistics\n")

    for dept, count in records:
        print(f"{dept} : {count} employees")

    conn.close()


def salary_statistics():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
    MAX(SALARY),
    MIN(SALARY),
    AVG(SALARY),
    SUM(SALARY)
    FROM EMPLOYEE
    """)

    max_sal, min_sal, avg_sal, total = cursor.fetchone()

    print("\nSalary Statistics\n")

    print("Highest Salary :", max_sal)
    print("Lowest Salary :", min_sal)
    print("Average Salary :", round(avg_sal, 2))
    print("Total Payroll Cost :", total)

    conn.close()


def total_employees():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM EMPLOYEE")

    total = cursor.fetchone()[0]

    print("\nTotal Employees :", total)

    conn.close()
