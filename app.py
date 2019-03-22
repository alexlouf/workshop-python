import sqlite3
import numpy as np


from flask import Flask, flash, redirect, render_template, request, session, abort
import os


app = Flask(__name__)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        with sqlite3.connect('ma_base.db') as con:
            cursor = con.cursor()

            cursor.execute("""CREATE TEMPORARY TABLE list_id_user (
                id INT)""")
            cursor.execute("""
                SELECT
                    ua.id_users
                FROM
                    users_alergie ua
                WHERE
                    ua.id_alergie NOT IN
                        (SELECT
                            compatibility_table.id_alergie_2
                        FROM
                            not_compatible_alergie compatibility_table
                        WHERE
                            compatibility_table.id_alergie_1 IN
                                (SELECT
                                    base_user_allergies.id_alergie
                                FROM
                                    users_alergie base_user_allergies
                                WHERE
                                    base_user_allergies.id_users=1)
                        )
                AND
                    ua.id_users != 1
            """)

            fatRequete = cursor.fetchall()
            examples = fatRequete
            cursor.executemany("INSERT INTO list_id_user VALUES (?)", examples)
            fatRequeteazer = cursor.fetchall()
            cursor.execute("SELECT * FROM list_id_user ")
            contientIdUser = cursor.fetchall()
            cursor.execute("""
            SELECT   id
            FROM     list_id_user
            GROUP BY id
            HAVING   COUNT(id) = (SELECT
                                    base_user_allergies.id_alergie
                                FROM
                                    users_alergie base_user_allergies)
            """)
            allUsers = cursor.fetchall()
            a = []
            for user in allUsers:
                cursor.execute("""SELECT * FROM users WHERE users.id_users = ?""", user)
                innerJoin = cursor.fetchall()
                a.extend(innerJoin)

            array = np.asarray(a)


        return render_template('match.html', users=array)


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
