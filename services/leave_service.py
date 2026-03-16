from database.connection import get_connection
from utils.logger import log_activity


def apply_leave(empid, from_date, to_date, reason):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO LEAVE_REQUEST
    (EMPID,FROM_DATE,TO_DATE,REASON,STATUS)
    VALUES(?,?,?,?,?)
    """, (empid, from_date, to_date, reason, "Pending"))

    conn.commit()
    log_activity(f"Leave Applied by EMPID {empid}")
    conn.close()

    print("Leave Applied")


def view_pending_leaves():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM LEAVE_REQUEST WHERE STATUS='Pending'"
    )

    records = cursor.fetchall()

    if records:
        for row in records:
            print(row)
    else:
        print("No pending leaves")

    conn.close()


def approve_leave(leaveid):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE LEAVE_REQUEST SET STATUS='Approved' WHERE LEAVEID=?",
        (leaveid,)
    )

    conn.commit()
    log_activity(f"Leave Approved: {leaveid}")
    conn.close()

    print("Leave Approved")


def reject_leave(leaveid):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE LEAVE_REQUEST SET STATUS='Rejected' WHERE LEAVEID=?",
        (leaveid,)
    )

    conn.commit()
    conn.close()

    print("Leave Rejected")
