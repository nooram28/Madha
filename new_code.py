import sqlite3

class Student:
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection established to SQLite database.")
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS students
                          (id INTEGER PRIMARY KEY, name TEXT, address TEXT)''')
        print("Table created successfully.")
    except sqlite3.Error as e:
        print(e)

def insert_student(conn, student):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (id, name, address) VALUES (?, ?, ?)",
                       (student.id, student.name, student.address))
        conn.commit()
        print("Student inserted successfully.")
    except sqlite3.Error as e:
        print(e)

def update_student(conn, student):
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE students SET name = ?, address = ? WHERE id = ?",
                       (student.name, student.address, student.id))
        conn.commit()
        print("Student updated successfully.")
    except sqlite3.Error as e:
        print(e)

def delete_student(conn, student_id):
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()
        print("Student deleted successfully.")
    except sqlite3.Error as e:
        print(e)

def display_menu():
    print("\nMENU:")
    print("1. Insert Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Exit")

def main():
    database = "students.db"
    conn = create_connection(database)
    if conn is not None:
        create_table(conn)
        while True:
            display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                id = int(input("Enter student ID: "))
                name = input("Enter student name: ")
                address = input("Enter student address: ")
                student = Student(id, name, address)
                insert_student(conn, student)
            elif choice == '2':
                id = int(input("Enter student ID to update: "))
                name = input("Enter updated name: ")
                address = input("Enter updated address: ")
                student = Student(id, name, address)
                update_student(conn, student)
            elif choice == '3':
                id = int(input("Enter student ID to delete: "))
                delete_student(conn, id)
            elif choice == '4':
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

        conn.close()
    else:
        print("Error! Cannot establish connection to the database.")

if __name__ == '__main__':
    main()
