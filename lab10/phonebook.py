import psycopg2
import csv
import os


conn = psycopg2.connect(
    host='localhost', 
    dbname='supplier', 
    user='postgres', 
    password='1202'
    )
def connect_db():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        return conn
    except psycopg2.Error as e:
        print("Error connecting to PostgreSQL", e)
        return None


# Design the PhoneBook table
def create_phonebook_table(cur):
    cur.execute('''
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            phone VARCHAR(20) UNIQUE NOT NULL
        )
    ''')
    cur.connection.commit()



def insert_data_from_csv(cur, csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            try:
                cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (row[0], row[1]))
            except psycopg2.IntegrityError:
                cur.connection.rollback()
                print(f"Duplicate entry for phone: {row[1]}")
            else:
                cur.connection.commit()




def insert_data_from_console(cur):
    username = input("Enter username: ")
    phone = input("Enter phone: ")
    try:
        cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (username, phone))
        cur.connection.commit()
        print("Data inserted successfully.")
    except psycopg2.IntegrityError:
        cur.connection.rollback()
        print("Phone number already exists in the phonebook.")



def update_user_info(cur):
    print("Choose update option:")
    print("1. Update username")
    print("2. Update phone")
    option = input("Select option (1 or 2): ")

    if option == '1':
        old_name = input("Enter existing username: ")
        new_name = input("Enter new username: ")
        cur.execute("UPDATE phonebook SET username = %s WHERE username = %s", (new_name, old_name))
    elif option == '2':
        old_phone = input("Enter existing phone number: ")
        new_phone = input("Enter new phone number: ")
        cur.execute("UPDATE phonebook SET phone = %s WHERE phone = %s", (new_phone, old_phone))

    cur.connection.commit()
    print("Data updated successfully.")


def query_phonebook(cur):
    print("Query phonebook by:")
    print("1. Username")
    print("2. Phone")
    option = input("Select option (1 or 2): ")

    if option == '1':
        username = input("Enter username to search: ")
        cur.execute("SELECT * FROM phonebook WHERE username = %s", (username,))
    elif option == '2':
        phone = input("Enter phone number to search: ")
        cur.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))

    results = cur.fetchall()
    if results:
        for row in results:
            print(f"ID: {row[0]}, Username: {row[1]}, Phone: {row[2]}")
    else:
        print("No records found.")


def delete_from_phonebook(cur):
    print("Delete by:")
    print("1. Username")
    print("2. Phone")
    option = input("Select option (1 or 2): ")

    if option == '1':
        username = input("Enter username to delete: ")
        cur.execute("DELETE FROM phonebook WHERE username = %s", (username,))
    elif option == '2':
        phone = input("Enter phone number to delete: ")
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))

    cur.connection.commit()
    print("Record(s) deleted successfully.")



def main():
    conn = connect_db()
    if conn is None:
        return

    cur = conn.cursor()
    create_phonebook_table(cur)

    insert_data_from_console(cur)  

    query_phonebook(cur)  
    
    update_user_info(cur)  

    delete_from_phonebook(cur)  

    cur.close()
    conn.close()


main()
