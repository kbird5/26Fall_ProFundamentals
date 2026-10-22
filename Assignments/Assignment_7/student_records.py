import sqlite3

conn = sqlite3.connect("student records")
cur = conn.cursor()

# conn.close()
print("\nDone")

#---Create the table---

cur.execute("DROP TABLE IF EXISTS StudentRecords")

cur.execute("""
        CREATE TABLE StudentRecords
        (id     INTEGER PRIMARY KEY AUTOINCREMENT,
         name   VARCHAR(30)  NOT NULL,
         age    INT,
         major  VARCHAR(20))
""")
print("Table created.")

#---Add rows---
cur.execute("""
    INSERT INTO StudentRecords
    Values(1, 'Maya', 18, 'Biology')
""")
initial_students = [
    (2, 'Leo', 21, 'History'),
    (3, 'Ana', 19, 'Biology'),
    (4, 'Sam', 22, 'Math'),
    (5, 'Priya', 20, 'Computer Science'),
]
query = "INSERT INTO StudentRecords VALUES (?, ?, ?, ?)"
cur.executemany(query, initial_students)

conn.commit()
print("Students added")

# print each student's anme, age, and major (do not print ID)

cur.execute("SELECT name, age, major FROM StudentRecords")
rows = cur.fetchall()
print("Current Students:")
for name, age, major in rows:
    print(f"Name: {name}, Age: {age}, Major: {major}")
    
# Asking the user if they want to add another student.
while True:
    response = input("\nDo you want to add a new student? (yes/no): ").lower()
    if response in ["yes", "no"]:
        break
    print("Invalid input. Please enter 'yes' or 'no'.")

if response == "yes":
    #ask for the student's name
    while True:
        name_input = input("Enter student's name: ")
        if name !="":
            break
        print("Name cannot be empty. Please try again.")
    #ask for the student's age
    while True:
        age_input = input("Enter the student's age: ")
        if age > 18:
            break
        else:
            print("Age must be 18 years or older.")
    #ask for the new student's major
    while True:
        major_input = input("Enter the student's major: ")
        if major !="":
            break
        print("Major cannot be empty. Please try again.")
# Insert the new student using ? placeholders (ID is handled automatically buy Autoincrement / unused ID)

query = "INSERT INTO StudentRecords (name, age, major) VALUES (?, ?, ?)"
new_student = (name_input, int(age_input), major_input)
cur.execute(query, new_student)
print("New student added successfully!")

#read rows with new student added
print("Current and New Students:")
cur.execute("SELECT * FROM StudentRecords")
rows = cur.fetchall()
for id, name, age, major in rows:
    print(f" ID: {id}, Name: {name}, Age: {age}, Major: {major}")


#commit changes and close the database connection
conn.commit()
conn.close()