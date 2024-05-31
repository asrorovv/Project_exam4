from classes import Students
from db import Check


def ent():
    student = input("""
        1. Login
        2. Register
            >>> """)

    if student == "1":
        return login()

    elif student == "2":
        return register()

    else:
        print("Error")
        return ent()


def register():
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    username = input("Username: ")
    password0 = input("Password: ")
    password1 = input("Password: ")
    while password0 != password1:
        print("Error!")
        password0 = input("Password: ")
        password1 = input("Reply Password: ")

    new_customer = Students(first_name, last_name, username, password0)
    print(new_customer.insert())
    return login()


def login():
    username = input("Username: ")
    password = input("Password: ")
    if Check.check(username, password):
        return site(username, password)

    else:
        print("Error")
        return login()


def site(username, password):
    enter = input("""

            1. Courses
            2. Instructors
            3. Personal info
            s. search
                >>> """)

    if enter == "1":
        pass
    elif enter == "2":
        pass
    else:
        print("Error")
        return site(username, password)


if __name__ == "__main__":
    ent()