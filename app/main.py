from flask import Flask, redirect, url_for, request, render_template, session
from app.db import *
import json

app = Flask(__name__)


@app.route('/')  # root route
def temp():
    return redirect(url_for('home'))  # Redirect to home page


@app.route('/home')  # home route
def home():
    return render_template('home.html')  # Render home page


@app.route('/search', methods=['POST', 'GET'])  # search route
def search():
    if request.method == 'POST':  # If request method is POST
        user = request.form['nm']  # Get username from form
        # Redirect to portfolio page
        return redirect(url_for('portfolio', name=user))
    else:
        return '404 ERROR'


@app.route('/login', methods=['POST', 'GET'])  # login route
def login():
    if request.method == 'POST':  # If request method is POST
        if request.args.get("f") == "lgn":  # If request args is lgn
            em = request.form['id']  # Get email from form
            pwd = request.form['pwd']  # Get password from form
            if get_user(em, pwd):  # If user exists
                session['username'] = get_user_name(em)  # Set session username
                # Redirect to portfolio page
                return redirect(url_for('portfolio', name=session['username']))
            else:
                # Render login page with error
                return render_template('login.html', error="Invalid username or password")
        else:  # If request args is not lgn means signup
            uname = request.form['unm']  # Get username from form
            sid = request.form['sid']  # Get student id from form
            spwd = request.form['spwd']  # Get password from form
            new_user(uname, sid, spwd)  # Add new user to database
            if get_user(sid, spwd):  # If user exists
                # Render login page with login now
                return render_template('login.html', inp='login now')
            else:
                return render_template('login.html')  # Render login page
    else:
        return render_template('login.html')  # Render login page


@app.route('/portfolio/<name>')  # portfolio route view only
def portfolio(name):
    if 'url' in session:  # If url exists in session
        session.pop('url', None)  # Remove url from session
    session['url'] = url_for('portfolio', name=name)  # Set url to session
    nav = get_nav(name)  # Get navigation from database
    # If username exists in session and session username is equal to name
    if 'username' in session and session['username'] == name:
        username = session['username']  # Set username to session username
        # Render portfolio page with navigation, name, username
        return render_template('portfolio.html', navigation=nav, name=name, username=username)
    else:
        # Render portfolio page with navigation, name
        return render_template('portfolio.html', navigation=nav, name=name)


# portfolio route edit only
@app.route('/portfolio/<name>/edit', methods=['POST', 'GET'])
def edit(name, refresh=False):  # refresh is used to refresh the page
    if refresh == True:
        return redirect(url_for('edit', name=name))  # Redirect to edit page
    if 'url' in session:  # If url exists in session
        session.pop('url', None)
    session['url'] = url_for('edit', name=name)  # Set url to session
    # If username exists in session and session username is equal to name
    if 'username' in session and session['username'] == name:
        nav = get_nav(name)  # Get navigation from database
        # Render portfolio page with navigation, name, username, edit
        return render_template('portfolio.html', navigation=nav, name=name, username=session['username'], edit=True)

    return redirect(url_for('home'))  # Redirect to home page


@app.route('/logout')
def logout():  # logout from the session
    name = session['username']  # Get username from session
    session.clear()  # Clear session
    # Redirect to portfolio page
    return redirect(url_for('portfolio', name=name))


# process_info route
@app.route('/process_info/<string:userinfo>', methods=['POST'])
def process_info(userinfo):  # userinfo is the username
    info = json.loads(userinfo)  # Load json data
    print(info)  # Print info
    # If username exists in session and session username is equal to info[3]
    if 'username' in session and session['username'] == info[3]:
        if info[2] == 'text':  # If type is text
            # Create div with style and text
            n = '<div style="{}">{}</div>'.format(info[1], info[0])
            new_nav(info[3], n)  # Add new navigation to database
        elif info[2] == 'image':  # If type is image
            temp = ''
            for i in info[0]:  # Loop through url
                if i == '^':  # If i is ^
                    temp += '/'  # Add / to temp
                else:
                    temp += i  # Add i to temp
            n = '<img src="{}" style="{}">'.format(
                temp, info[1])  # Create img with src and style
            print(n)  # Print n
            new_nav(info[3], n)  # Add new navigation to database
        elif info[2] == 'del':  # If type is del
            del_nav(info[3], info[0])  # Delete navigation from database
        elif info[2] == 'delimg':  # If type is delimg
            temp = ''
            # Loop through url and replace encoded ^ with / which was used to send url as a request
            for i in info[0]:
                if i == '^':
                    temp += '/'
                else:
                    temp += i
            del_nav(info[3], temp)  # Delete navigation from database
        # sleep(1)
        return redirect(session['url'])  # Redirect to session url
    return redirect(session['url'])  # Redirect to session url


@app.route('/about')  # about route
def about():
    return render_template('about.html')  # Render about page
