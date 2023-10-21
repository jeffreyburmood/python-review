""" main application to use the database """

import database


def menu():
    connection = database.connect()
    database.create_tables(connection)
