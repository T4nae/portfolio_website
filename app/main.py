from flask import Flask, redirect, url_for, request, render_template, make_response, session, flash
app = Flask(__name__)

@app.route('/')
def temp():
    return render_template('temp.html')

