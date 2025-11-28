import sqlite3
# Shreyash F090
# Step 1: Connect to database
# -----------------------------
conn = sqlite3.connect("Shreyash.db")
cursor = conn.cursor()
print("Database connected successfully!")

# Shreyash F090
# Step 2: Create Table
# -----------------------------
cursor.execute("""
CREATE TABLE  F090_2 (
    Name TEXT,
    Age INTEGER,
    City TEXT,
    Grade TEXT
)
""")
print("Table created successfully!")

# Shreyash F090
# Step 3: Insert Values
# -----------------------------
cursor.execute("INSERT INTO F090_2 VALUES (?, ?, ?, ?)", ("Shreyash", 17, "Mumbai", "FYCS"))
cursor.execute("INSERT INTO F090_2 VALUES (?, ?, ?, ?)", ("Om", 18, "Pune", "FYBA"))
cursor.execute("INSERT INTO F090_2 VALUES (?, ?, ?, ?)", ("Krish", 17, "Vile Parle", "FYCS"))
cursor.execute("INSERT INTO F090_2 VALUES (?, ?, ?, ?)", ("Palak", 17, "Andheri", "FYCS"))
conn.commit()
print("Values inserted successfully!")

# Shreyash F090
# Step 5: UPDATE Record
# -----------------------------
cursor.execute("UPDATE F090_2 SET City = ? WHERE Name = ?", ("Thane", "Palak"))
conn.commit()
print("\nRecord updated successfully!")

# Shreyash F090
# -----------------------------
cursor.execute("SELECT * FROM F090_2")
print("\nBefore Delete:")
for row in cursor.fetchall():
    print(row)

# Shreyash F090
# Step 5: DELETE Record
# -----------------------------
cursor.execute("DELETE FROM F090_2 WHERE Name = ?", ("Shreyash",))
conn.commit()
print("\nRecord deleted successfully!")

# Shreyash F090
# Step 
# -----------------------------
cursor.execute("SELECT * FROM F090_2")
print("\nAfter Delete:")
for row in cursor.fetchall():
    print(row)


conn.close()
print("\nConnection closed.")
