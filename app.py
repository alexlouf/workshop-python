import sqlite3

from flask import Flask, flash, redirect, render_template, request, session, abort
import os


app = Flask(__name__)

# connexion db
conn = sqlite3.connect('ma_base.db')
cursor = conn.cursor()
conn.execute("PRAGMA foreign_keys = ON")


def getlog(mail, mdp):
    cursor.execute("""SELECT COUNT(*) FROM users WHERE email = ? AND password = ?""", (mail, mdp))
    login = cursor.fetchall()
    return login.pop()[0]


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('match.html')


@app.route('/login', methods=['POST'])
def do_admin_login():
    mail = request.form['username']
    mdp = request.form['password']
    with sqlite3.connect("ma_base.db") as con:
        cur = con.cursor()
        cur.execute("SELECT COUNT(*) FROM users WHERE email = ? AND password = ?", (mail, mdp))
        login = cur.fetchall().pop()[0]

    if login != 0:
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return redirect('/')




@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect('/')


@app.route("/signin")
def signin():
    return render_template("signin.html")


@app.route("/validatesignin", methods=['POST'])
def validatesignin():
    session['logged_in'] = False
    print(request.form)
    return redirect('/')


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.debug = True
    app.run()
