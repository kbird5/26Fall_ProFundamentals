import sqlite3

conn = sqlite3.connect("student records")
cur = conn.cursor()

# conn.close()
print("\nDone")

#---Create the table---

cur.execute("DROP TABLE IF EXISTS student records")

cur.execute