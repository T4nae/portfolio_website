from flask import Flask, redirect, url_for, request, render_template, make_response, session, flash
from app.db import *
import json
from time import sleep
app = Flask(__name__)

@app.route('/')
def temp():
    return redirect(url_for('home'))

@app.route('/home')
def home():
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
    print(session['url'])
    nav = get_nav(name)
    if 'username' in session and session['username'] == name:
        username = session['username']
        return render_template('portfolio.html', navigation = nav, name = name, username = username)
    else:
        return render_template('portfolio.html', navigation = nav, name = name)

@app.route('/portfolio/<name>/edit', methods = ['POST', 'GET'])
def edit(name, refresh = False):
    if refresh == True:
        return redirect(url_for('edit', name = name))
    if 'url' in session:
        session.pop('url', None)
    session['url'] = url_for('edit', name = name)
    print(session['url'])
    if 'username' in session and session['username'] == name:
            nav = get_nav(name)
            return render_template('portfolio.html', navigation = nav, name = name, username = session['username'], edit= True)
    
    return redirect(session['url'])

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(session['url'])

@app.route('/process_info/<string:userinfo>', methods = ['POST'])
def process_info(userinfo):
    info = json.loads(userinfo)
    print(info)
    if 'username' in session and session['username'] == info[3]:
        if info[2] == 'text':
            n = '<div style="{}">{}</div>'.format(info[1], info[0])
            new_nav(info[3], n)
        elif info[2] == 'image':
            temp = ''
            for i in info[0]:
                if i == '^':
                    temp += '/'
                else:
                    temp += i
            n = '<img src="{}" style="{}">'.format(temp, info[1])
            print(n)
            new_nav(info[3], n)
        elif info[2] == 'del':
            del_nav(info[3], info[0])
        elif info[2] == 'delimg':
            temp = ''
            for i in info[0]:
                if i == '^':
                    temp += '/'
                else:
                    temp += i
            del_nav(info[3], temp)
        #sleep(1)
        return redirect(session['url'])
    return redirect(session['url'])
