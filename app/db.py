import sqlite3 as sql

def new_user(username, id, password):
    con = sql.connect('user.db')
    cur = con.cursor()
    cur.execute("INSERT INTO users VALUES (?,?,?)", (username, id, password))
    con.commit()
    con.close()

def create_user_db():
    con = sql.connect('user.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, id TEXT, password TEXT)")
    con.commit()
    con.close()

def get_user(id, password):
    con = sql.connect('user.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    con.close()
    for row in rows:
        if row[1] == id and row[2] == password:
            return True
    return False
