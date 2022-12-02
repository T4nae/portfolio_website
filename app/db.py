import sqlite3 as sql

def create_user_db():
    con = sql.connect('DB/user.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, id TEXT, password TEXT)")
    con.commit()
    con.close()

def new_user(username, id, password):
    con = sql.connect('DB/user.db')
    cur = con.cursor()
    cur.execute("INSERT INTO users VALUES (?,?,?)", (username, id, password))
    con.commit()
    con.close()

def get_user(id, password):
    con = sql.connect('DB/user.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    con.close()
    for row in rows:
        if row[1] == id and row[2] == password:
            return True
    return False

def create_navigation_db():
    con = sql.connect('DB/navigation.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS navigation (username TEXT nav TEXT)")
    con.commit()
    con.close()

def new_nav(username, nav):
    con = sql.connect('DB/navigation.db')
    cur = con.cursor()
    cur.execute("INSERT INTO navigation VALUES (?,?)", (username, nav))
    con.commit()
    con.close()

def get_nav(username):
    con = sql.connect('DB/navigation.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM navigation WHERE username = ?", (username,))
    rows = cur.fetchall()
    con.close()
    return rows