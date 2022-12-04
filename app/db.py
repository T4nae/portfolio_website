import sqlite3 as sql

def create_user_db():
    con = sql.connect('DB/users.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, id TEXT, password TEXT)")
    con.commit()
    con.close()

def new_user(username, id, password):
    con = sql.connect('DB/users.db')
    cur = con.cursor()
    cur.execute("INSERT INTO users VALUES (?,?,?)", (username, id, password))
    con.commit()
    con.close()

def get_user(id, password):
    con = sql.connect('DB/users.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    con.close()
    for row in rows:
        if row[1] == id and row[2] == password:
            return True
    return False

def get_user_name(id):
    con = sql.connect('DB/users.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE id = ?", (id,))
    rows = cur.fetchall()
    con.close()
    return rows[0][0]

def create_navigation_db():
    con = sql.connect('DB/navigation.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS navigation (username TEXT, nav TEXT)")
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
    cur.execute("SELECT nav FROM navigation WHERE username = ?", (username,))
    rows = cur.fetchall()
    con.close()
    r = []
    for row in rows:
        r.append(row[0])
    return r

def del_nav(username, nav):
    con = sql.connect('DB/navigation.db')
    cur = con.cursor()
    for i in get_nav(username):
        if i.split('>')[1].split('<')[0] == nav:
            cur.execute("DELETE FROM navigation WHERE username = ? AND nav = ?", (username, i))
            break
        elif i.split('"')[1] == nav:
            cur.execute("DELETE FROM navigation WHERE username = ? AND nav = ?", (username, i))
            break
    con.commit()