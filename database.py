import sqlite3

DATABASE_NAME = "database.db"


def create_database():
    connection = sqlite3.connect(DATABASE_NAME)

    with open("schema.sql", "r") as file:
        connection.executescript(file.read())

    connection.close()

    print("Database created successfully.")


if __name__ == "__main__":
    create_database()