from flask import Flask, redirect, url_for, request, render_template, make_response, session, flash
from app.db import new_user, get_user
app = Flask(__name__)

@app.route('/')
def temp():
    return render_template('temp.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.args.get("f") == "lgn":
            em = request.form['id']
            pwd = request.form['pwd']
            if get_user(em, pwd):
                return render_template('temp.html', inp = get_user(em, pwd))
            else:
                return render_template('login.html', error = "Invalid username or password")
        else:
            uname = request.form['unm']
            sid = request.form['sid']
            spwd = request.form['spwd']
            new_user(uname, sid, spwd)
            if get_user(sid, spwd):
                return render_template('login.html', inp= 'login now')
            else:
                return render_template('login.html')
    else:
        return render_template('login.html')