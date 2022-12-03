from flask import Flask, redirect, url_for, request, render_template, make_response, session, flash
from app.db import *
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
                session['username'] = get_user_name(em)
                return redirect(url_for('portfolio', name = session['username']))
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
"""
use temp mail for testing
qwerty
test@mail.com
1234567890
"""
@app.route('/portfolio/<name>')
def portfolio(name):
    if 'url' in session:
        session.pop('url', None)
    session['url'] = url_for('portfolio', name = name)
    nav = get_nav(name)
    if 'username' in session and session['username'] == name:
        username = session['username']
        return render_template('portfolio.html', navigation = nav, name = name, username = username)
    else:
        return render_template('portfolio.html', navigation = nav, name = name)

@app.route('/portfolio/<name>/edit', methods = ['POST', 'GET'])
def edit(name):
    if 'username' in session and session['username'] == name:
        if request.method == 'POST':
            text = request.form['text']
            css = request.form['css']
            n = '<div style="{}">{}</div>'.format(css, text)
            new_nav(name, n)
            nav = get_nav(name)[:]
            return render_template('portfolio.html', navigation = nav, name = name, username = session['username'], edit= True)
        else:
            nav = get_nav(name)
            return render_template('portfolio.html', navigation = nav, name = name, username = session['username'], edit= True)
    
    return redirect(session['url'])

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(session['url'])