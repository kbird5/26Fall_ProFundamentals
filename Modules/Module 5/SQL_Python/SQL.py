import sqlite3

conn = sqlite3.connect("school.db")
cur = conn.cursor()

print("\nDone.")

cur.execute("DROP TABLE IF EXISTS students")


cur.execute("""
    CREATE TABLE students
    ( id      INT          NOT NULL,
      name    VARCHAR(30)  NOT NULL,
      age     INT,
      major   VARCHAR(20),
      credits INT,
      email   VARCHAR(40),
      PRIMARY KEY (id))
""")

cur.execute("""
    INSERT INTO students
    VALUES (1, 'Maya', 18, 'Biology', 15, 'mya@example.edu')
""")

students = [
    (2, 'Leo', 21, 'History', 45, None),
    (3, 'Ana', 19, 'Biology', 30, 'ana@example.edu'),
    (4, 'Sam', 22, 'Math', 60, None),
    (5, 'Priya', 20, 'Computer Science', 40, 'prya@example.edu'),
    (6, 'Omar', 18, 'Math', 12, 'omar@example.edu'),
    (7, 'Mia', 23, 'History', 75, 'mia@example.edu'),
    (8, 'Jon', 19, 'Computer Science', 28, None),
]
query = "INSERT INTO students Values (?, ?, ?, ?, ?, ?)"
cur.executemany(query, students)
conn.commit()
print("Students added.")

print("\nEvery student:")
cur.execute("Select * FROM students")
rows = cur.fetchall()
for row in rows:
    print(row)

print("\nStudents aged 20 or older:")
cur.execute("SELECT name, age FROM students WHERE age >= 20")
for row in cur.fetchall():
    print(row)

major = "Math"
print("\nStudents in", major)
cur.execute("SELECT name FROM students WHERE major =?", (major,))
for row in cur.fetchall():
    print(row)

print("\nAND: Biology students under 19")
query = "SELECT name FROM students WHERE major = 'Biology' AND age <19"
for row in cur.execute(query):
    print(row)

print("\nOR: Math students, or anyone with over 50 credits")
query = "SELECT name FROM students WHERE major ='Math' OR credits >50"
for row in cur.execute(query):
    print(row)

print("\nNOT: students not in Hisotry")
query = "SELECT name FROM students WHERE NOT major = 'History'"
for row in cur.execute(query):
    print(row)



conn.close()    
