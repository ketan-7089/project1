from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database setup
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS books
             (id INTEGER PRIMARY KEY, title TEXT, author TEXT)''')

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Handle login logic
    return render_template('login.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    # Handle sign-in logic
    return redirect(url_for('index'))

@app.route('/books')
def books():
    # Fetch books from the database
    c.execute("SELECT * FROM books")
    books = c.fetchall()
    return render_template('books.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
