""" main application to use the database """

import database

MENU_PROMPT = """
    Please choose one of these options:
    
    1) Add a new bean
    2) See all beans
    3) Find a bean by name
    4) See which preparation method is best
    5) Exit
    
"""


def menu():
    connection = database.connect()
    database.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "5":
        if user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            print("Invalid input, please try again")


menu()
