import sqlite3

# Path to the SQLite database file
db_path = r'C:\Users\aksha\OneDrive\Documents\Task\WELLENCE_projectDjango\db.sqlite3'

# Connect to the SQLite database
conn = sqlite3.connect(db_path)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Get a list of all tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Print the list of tables
print("Tables in the database:")
for i, table in enumerate(tables):
    print(f"{i + 1}: {table[0]}")

# Prompt user to select a table
table_index = int(input("\nEnter the number of the table you want to query: ")) - 1

# Get the selected table name
table_name = tables[table_index][0]

# Query data from the selected table
cursor.execute(f"SELECT * FROM {table_name};")
rows = cursor.fetchall()

# Print the data from the selected table
print(f"\nData from table {table_name}:")
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
