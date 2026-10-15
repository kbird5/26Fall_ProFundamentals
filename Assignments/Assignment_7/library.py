import sqlite3 # accesses sqlite3 module

conn = sqlite3.connect("library.db") #opens a connection to library.db
cur = conn.cursor() # runs SQL commands

# conn.close() # closes the connection to library.db
print("\nDone.")


#----Creating table----
cur.execute("DROP TABLE IF EXISTS library") # deletes table if it exists and allows for the program to loop vs only be ran once.

cur.execute("""
    CREATE TABLE library
    (id       INT,
     title    VARCHAR(40),
     author   VARCHAR(30),
     year     INT,
     genre    VARCHAR(20),
     copies   INT,
     rating   INT,
     PRIMARY  KEY (id))
""")
print("Table created.")

#----Adding data to table----
cur.execute("""
    INSERT INTO library
    VALUES (1, 'The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Fiction', 3, 5)
""")
NULL = None # sets NULL to None for python

books = [
    (2, 'To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction', 5, 5),
    (3, '1984', 'George Orwell', 1949, 'Dystopian', 4, 5),
    (4, 'Pride and Prejudice', 'Jane Austen', 1813, 'Romance', 2, NULL),
    (5, 'The Catcher in the Rye', 'J.D. Salinger', 1951, 'Fiction', 3, NULL),
    (6, 'The Hobbit', 'J.R.R. Tolkien', 1937, 'Fantasy', 6, 5),
    (7, 'The Lord of the Rings', 'J.R.R. Tolkien', 1954, 'Fantasy', 5, 5),
    (8, 'The Chronicles of Narnia', 'C.S. Lewis', 1950, 'Fantasy', 4, 5),
    (9, 'The Da Vinci Code', 'Dan Brown', 2003, 'Thriller', 3, 4),
    (10, 'The Hunger Games', 'Suzanne Collins', 2008, 'Dystopian', 5, NULL),
    (11, 'The Naval War of 1812', 'Theodore Roosevelt', 1882, 'Hisotry', 2, NULL),
    (12, 'Experiments on Plant Hybridization', 'Gregor Mendel', 1866, 'Science', 3, 2)
]
query = "INSERT INTO library VALUES (?, ?, ?, ?, ?, ?, ?)"
cur.executemany(query, books)
conn.commit() # commits changes to data base

print("Data added to table.")


#---Print the title and author of books published after 1990---
print("\nTitle and author of books published after 1990:")
cur.execute("SELECT title, author FROM library WHERE year > 1990") # selects title and author of books published after 1990
for row in cur.fetchall():
    print(row) # prints the title and author of books published after 1990

#---Print the title of fiction books with more than 2 copies (AND)---
print("\nTitle of fiction books with more than 2 copies:")
cur.execute("SELECT title FROM library WHERE genre = 'Fiction' AND copies >2") # selects title of fiction books with more than 2 copies
for row in cur.fetchall():
    print(row) # prints the title of fiction books with more than 2 copies

#---Print the title of books published before 1900 or rated 5 (OR)---
print("\nTitle of books published before 1900 or rated 5:")
cur.execute("SELECT title FROM library WHERE year < 1900 OR rating = 5") # selects title of books published before 1900 or rated 5
for row in cur.fetchall():
    print(row) # prints the title of books published before 1900 or rated 5

#---Print the title of books that are NOT in the Mystery genre (NOT)---
print("\nTitle of books that are NOT in the Mystery genre")
cur.execute("SELECT title FROM library WHERE genre != 'Mystery'") # selects title of books that are NOT in the Mystery genre
for row in cur.fetchall():
    print(row) # prints the title of books that are NOT in the Mystery genre

#---Print the title of books in either the Science or History genre (IN)---
print("\nTitle of books in either the Science or History genre:")
cur.execute("SELECT title FROM library WHERE genre IN ('Science', 'History')") # selects title of books in either the Science or History genre
for row in cur.fetchall():
    print(row) # prints the title of books in either the Science or History genre

#---Ask the user for a letter, then print the authors whose names start with that letter (LIKE). Pass the letter with a ? placeholder.---
user_letter = input("\nEnter a letter to search authors: ")
search_pattern = f"{user_letter.upper()}%"
query = "SELECT author FROM library WHERE UPPER(author) LIKE ?"
cur.execute(query, (search_pattern,))
results = cur.fetchall()
print(f"\nAuthors starting with '{user_letter}':") # prints the author who has a letter starting with user input
# if user input is not part of the list
if results:
    for row in results:
        print(f"-{row[0]}")
else:
    print("No authors found matching that letter.")

#---Print the title of books that have no rating (IS NULL)---
print("\nTitle of books that have no rating:")
cur.execute("SELECT title FROM library WHERE rating IS NULL") # selects title of books that have
for row in cur.fetchall():
     print(row) # prints the title of books that have no rating

conn.close() # closes the connection to library.db