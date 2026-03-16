from database.connection import get_connection


def login(username, password):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT ROLE,EMPID FROM LOGIN WHERE USERNAME=? AND PASSWORD=?",
        (username, password)
    )

    user = cursor.fetchone()

    conn.close()

    return user


def create_user(username, password, role, empid=None):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO LOGIN(USERNAME,PASSWORD,ROLE,EMPID)
    VALUES(?,?,?,?)
    """, (username, password, role, empid))

    conn.commit()
    conn.close()

    print("User created successfully")
