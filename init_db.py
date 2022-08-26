import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content, group_no) VALUES (?, ?, ?)",
            ('First Post', 'Content for the first post', 1)
            )

cur.execute("INSERT INTO posts (title, content, group_no) VALUES (?, ?, ?)",
            ('Second Post', 'Content for the second post', 2)
            )

cur.execute("INSERT INTO posts (title, content, group_no) VALUES (?, ?, ?)",
            ('Third Post', 'Content for the third post', 1)
            )

cur.execute("INSERT INTO posts (title, content, group_no) VALUES (?, ?, ?)",
            ('Fourth Post', 'Content for the fourth post', 3)
            )

cur.execute("INSERT INTO posts (title, content, group_no) VALUES (?, ?, ?)",
            ('Fifth Post', 'Content for the fifth post', 4)
            )

connection.commit()
connection.close()
