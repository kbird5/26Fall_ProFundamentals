import sqlite3

conn = sqlite3.connect("student records")
cur = conn.cursor()

# conn.close()
print("\nDone")

#---Create the table---

cur.execute("DROP TABLE IF EXISTS StudentRecords")

cur.execute("""
        CREATE TABLE StudentRecords
        (id     INT          NOT NULL,
         name   VARCHAR(30)  NOT NULL,
         age    INT,
         major  VARCHAR(20),
         PRIMARY KEY (id))
""")
print("Table created.")

#---Add rows---
cur.execute("""
    INSERT INTO StudentRecords
    Values(1, 'Maya', 18, 'Biology')
""")
StudentRecords = [
    (2, 'Leo', 21, 'History'),
    (3, 'Ana', 19, 'Biology'),
    (4, 'Sam', 22, 'Math'),
    (5, 'Priya', 20, 'Computer Science'),
]
query = "INSERT INTO StudentRecords VALUES (?, ?, ?, ?)"
cur.executemany(query, StudentRecords)

conn.commit()
print("Students added")

print("nEvery student:")
cur.execute("SELECT name, age, major FROM StudentRecords")
rows = cur.fetchall()
for row in rows:
    print(row)

