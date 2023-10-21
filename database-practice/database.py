import sqlite3

connection = sqlite3.connect("practice-data.db")

with connection:
    connection.execute(
        "CREATE TABLE beans (id INTEGER PRIMARY KEY, name TEXT, method TEXT, rating INTEGER);"
    )