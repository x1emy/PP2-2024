# Connect to your PostgreSQL database
import psycopg2

# Use appropriate connection details
conn = psycopg2.connect(
    host='localhost',
    dbname='lab10',
    user='postgres',
    password='1202'
)

# Create a cursor
cur = conn.cursor()

# Delete rows from 'phonebook' where 'score' is 3
cur.execute("""
           DELETE FROM phonebook
           WHERE score = 3
""")

# Commit the changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
