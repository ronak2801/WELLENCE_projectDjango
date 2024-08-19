import sqlite3

db_path = r'C:\Users\aksha\OneDrive\Documents\Task\WELLENCE_projectDjango\db.sqlite3'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables in the database:")
for i, table in enumerate(tables):
    print(f"{i + 1}: {table[0]}")
table_index = int(input("\nEnter the number of the table you want to query: ")) - 1
table_name = tables[table_index][0]
cursor.execute(f"SELECT * FROM {table_name};")
rows = cursor.fetchall()
print(f"\nData from table {table_name}:")
for row in rows:
    print(row)

cursor.close()
conn.close()
