import psycopg2
#username = input("username: ")
#new_phone = input("phone number: ")

# Function that returns all records based on a pattern 
def search(table_name, column_name, pattern):
    try:
        conn = psycopg2.connect(
            host='localhost',
            dbname='lab10',
            user='postgres',
            password='1202'
        )
        
        cur = conn.cursor()

        query = f"SELECT * FROM phonebook WHERE username ILIKE %s"

        like_pattern = f"%{pattern}%"
        
        cur.execute(query, (like_pattern,))
        
        records = cur.fetchall()
        
        cur.close()
        conn.close()
        
    
        return records

    except Exception as e:
        print("An error has occurred:", e)
        return []

# Example usage
pattern = input("Enter a pattern to search: ")
results = search('phonebook', 'username', pattern)

# Display the results
if results:
    for record in results:
        print(record)
else:
    print("No records found matching the pattern.")

#Create procedure to insert new user by name and phone, update phone if user already exists
def update(username, new_phone):
    try:
        conn = psycopg2.connect(
            host='localhost',
            dbname= 'lab10',
            user='postgres', 
            password='1202')
        cur = conn.cursor()

        cur.execute("SELECT * FROM phonebook WHERE username = %s", (username,))
        user = cur.fetchone()

        if user:
            cur.execute("UPDATE phonebook SET phone = %s WHERE username = %s", (new_phone, username))
            conn.commit()
            print(f"Phone number for {username} updated.")
        else:
            cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (username, new_phone))
            conn.commit()
            print(f"Contact {username} added {new_phone}.")

        conn.close()
    except Exception as e:
        print("An error occurred:", e)

#Implement procedure to deleting data from tables by username or phone
def delete(name=None, phone=None):
    try:
        conn = psycopg2.connect(
            host='localhost',
            dbname= 'lab10',
            user='postgres', 
            password='1202')
        cur = conn.cursor()

        if name:
            cur.execute("DELETE FROM phonebook WHERE username ILIKE %s", (name,))
        elif phone:
            cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
        
        conn.commit()
        cur.close()
        conn.close()
        
        print("This contact was deleted")
    except Exception as e:
        print("An error has occurred:", e)

#delete(username)

#delete(new_phone)
