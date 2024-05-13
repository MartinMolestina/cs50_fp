from flask import Flask, render_template, request, redirect, session, url_for, g
import sqlite3
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['DATABASE'] = './database/database.db'

# Database connection
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(app.config['DATABASE'])
        db.row_factory = sqlite3.Row
    return db

# Close database connection
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# User registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        db.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        if user:
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')

# User logout
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('index'))

# Index page (requires login)
@app.route('/')
def index():
    if 'logged_in' in session:
        return f'Hello, {session["username"]}! <a href="/logout">Logout</a>'
    else:
        return 'You are not logged in. <a href="/login">Login</a>'

if __name__ == '__main__':
    app.run(debug=True)
