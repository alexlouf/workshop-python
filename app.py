from flask import Flask, flash, redirect, render_template, request, session, abort
import os


app = Flask(__name__)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('match.html')


@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
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
    print(request.form)
    return redirect('/')


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.debug = True
    app.run()
