from database.connection import get_connection


def create_tables():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS EMPLOYEE(
        EMPID INTEGER PRIMARY KEY AUTOINCREMENT,
        ENAME TEXT,
        DEPARTMENT TEXT,
        MOBILENUMBER INTEGER,
        SALARY INTEGER,
        JOIN_DATE TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ATTENDANCE(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        EMPID INTEGER,
        DATE TEXT,
        STATUS TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS LEAVE_REQUEST(
        LEAVEID INTEGER PRIMARY KEY AUTOINCREMENT,
        EMPID INTEGER,
        FROM_DATE TEXT,
        TO_DATE TEXT,
        REASON TEXT,
        STATUS TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS PAYROLL(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        EMPID INTEGER,
        BONUS INTEGER,
        TAX INTEGER,
        NETSALARY INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS LOGIN(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        USERNAME TEXT UNIQUE,
        PASSWORD TEXT,
        ROLE TEXT,
        EMPID INTEGER
    )
    """)

    cursor.execute("""
    INSERT INTO LOGIN(USERNAME,PASSWORD,ROLE)
    SELECT 'admin','admin123','admin'
    WHERE NOT EXISTS (SELECT 1 FROM LOGIN WHERE USERNAME='admin')
""")

    conn.commit()
    conn.close()
