import psycopg2
import csv
from config import load_config

def create_table():
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS PhoneBook (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100),
                    phone VARCHAR(20)
                )
            """)
            conn.commit()
            print("Table created (if it didn't exist).")

def insert_from_input():
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (name, phone))
            conn.commit()
            print("Data inserted from input.")

def upload_from_csv(filename):
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            with open(filename, 'r') as f:
                reader = csv.reader(f)
                next(reader)  # Skip header
                for row in reader:
                    cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", row)
            conn.commit()
            print("Data uploaded from CSV.")

def update_user():
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            username = input("Enter the username to update: ")
            new_phone = input("Enter new phone (leave blank to skip): ")
            new_name = input("Enter new name (leave blank to skip): ")

            if new_phone:
                cur.execute("UPDATE PhoneBook SET phone = %s WHERE name = %s", (new_phone, username))
            if new_name:
                cur.execute("UPDATE PhoneBook SET name = %s WHERE name = %s", (new_name, username))
            conn.commit()
            print("Data updated.")

def search_users():
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            keyword = input("Search by name or phone: ")
            cur.execute("SELECT * FROM PhoneBook WHERE name ILIKE %s OR phone ILIKE %s", (f'%{keyword}%', f'%{keyword}%'))
            rows = cur.fetchall()
            print("Search results:")
            for row in rows:
                print(row)

def delete_user():
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            value = input("Enter name or phone to delete: ")
            cur.execute("DELETE FROM PhoneBook WHERE name = %s OR phone = %s", (value, value))
            conn.commit()
            print("Data deleted.")

def menu():
    while True:
        print("PhoneBook Menu")
        print("1. Create table")
        print("2. Insert from input")
        print("3. Upload from CSV")
        print("4. Update user")
        print("5. Search users")
        print("6. Delete user")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            create_table()
        elif choice == '2':
            insert_from_input()
        elif choice == '3':
            filename = input("Enter CSV filename (e.g., contacts.csv): ")
            upload_from_csv(filename)
        elif choice == '4':
            update_user()
        elif choice == '5':
            search_users()
        elif choice == '6':
            delete_user()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    menu()
