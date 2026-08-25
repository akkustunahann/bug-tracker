import sqlite3

DATABASE_NAME = "database.db"

STATUS_FLOW = {
    "Created": "In Progress",
    "In Progress": "Done",
    "Done": None
}


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def create_database():
    connection = get_connection()

    with open("schema.sql", "r") as file:
        connection.executescript(file.read())

    connection.close()

    print("Database created successfully.")


def create_bug(title, description, reported_by):

    connection = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO bugs (title, description, reported_by)
            VALUES (?, ?, ?)
        """, (title, description, reported_by))

        connection.commit()

        return True

    except sqlite3.Error as error:
        print("Database error:", error)
        return False

    finally:
        if connection:
            connection.close()


def get_all_bugs():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM bugs")

    bugs = cursor.fetchall()

    connection.close()

    return bugs


def update_bug_status(bug_id, new_status):

    connection = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT status
            FROM bugs
            WHERE id = ?
        """, (bug_id,))

        result = cursor.fetchone()

        if result is None:
            print("Bug not found.")
            return False

        current_status = result[0]

        allowed_next_status = STATUS_FLOW[current_status]

        if allowed_next_status != new_status:
            print(f"Invalid transition: {current_status} -> {new_status}")
            return False

        cursor.execute("""
            UPDATE bugs
            SET status = ?
            WHERE id = ?
        """, (new_status, bug_id))

        connection.commit()

        print("Status updated successfully.")

        return True

    except sqlite3.Error as error:
        print("Database error:", error)
        return False

    finally:
        if connection:
            connection.close()


def delete_bug(bug_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM bugs
        WHERE id = ?
    """, (bug_id,))

    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_database()