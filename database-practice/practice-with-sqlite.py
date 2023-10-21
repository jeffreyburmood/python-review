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


def print_bean_info(bean):
    print(f"name: {bean[1]}, method: {bean[2]}, rating: {bean[3]}")


def get_new_bean_inputs():
    name = input("Enter bean name: ")
    method = input("Enter preparation method: ")
    rating = int(input("Enter rating score (0-100): "))
    return name, method, rating

def get_bean_name():
    return input("Enter bean name of interest: ")


def menu():
    connection = database.connect()
    database.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "5":
        if user_input == "1":
            name, method, rating = get_new_bean_inputs()
            database.add_bean(connection, name, method, rating)
        elif user_input == "2":
            beans = database.get_all_beans(connection)
            for bean in beans:
                print_bean_info(bean)
        elif user_input == "3":
            bean_name = get_bean_name()

            beans = database.get_beans_by_name(connection, bean_name)
            for bean in beans:
                print_bean_info(bean)
        elif user_input == "4":
            bean_name = get_bean_name()

            bean = database.get_best_preparation_for_bean(connection, bean_name)
            print_bean_info(bean)
        else:
            print("Invalid input, please try again")


menu()