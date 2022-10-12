# From 50 days of Python Challenge book
import sqlite3

conn = sqlite3.connect('movies.db')
c = conn.cursor()

# Creating the Table

# c.execute(""" CREATE TABLE movies (
#                year integer,
#               title text,
#              genre text )""")

data = [
            (2009, 'Brothers', 'Drama'),
            (2002, 'Spider Man', 'Sci-fi'),
            (2009, 'WatchMen', 'Drama'),
            (2010, 'Inception', 'Sci-fi'),
            (2009, 'Avatar', 'Fantasy')
        ]

# Insert Records
c.executemany("INSERT INTO movies VALUES (?,?,?)", data)

c.execute("SELECT rowid, * FROM movies WHERE genre = 'Fantasy' OR genre = 'Drama'")
items = c.fetchall()
for item in items:
    print(item)

# Commit
conn.commit()

# Close connection
conn.close()
