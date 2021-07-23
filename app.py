import sqlite3

from flask import Flask, render_template


def init_sqlite_db():
    conn = sqlite3.connect("database.db")
    print("Opened database successfully")

    conn.execute("CREATE TABLE students IF NOT EXISTS (name TEXT, addr TEXT, city TEXT, pin TEXT)")
    print("Table created successfully")
    conn.close()


init_sqlite_db()

app = Flask(__name__)


@app.route('/enter-new/')
def enter_new_student():
    return render_template('student.html')
