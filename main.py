from database.setup import create_tables
from services.auth_service import login

from menus.superadmin_menu import superadmin_menu
from menus.hr_menu import hr_menu
from menus.employee_menu import employee_menu


def main():

    # Create database tables
    create_tables()

    print("\n========= HR MANAGEMENT LOGIN =========")

    username = input("Username: ")
    password = input("Password: ")

    user = login(username, password)

    if not user:
        print("Invalid login credentials. Exiting...")
        return

    role, empid = user

    print(f"\nLogin Successful! Welcome ({role.upper()})\n")

    # ROLE-BASED ROUTING
    if role == "superadmin":
        superadmin_menu()

    elif role == "hr":
        hr_menu()

    elif role == "employee":
        if empid is None:
            print("Error: No Employee ID linked to this account. Contact Admin.")
            return
        employee_menu(empid)

    else:
        print("Unknown role. Access denied.")


if __name__ == "__main__":
    main()
